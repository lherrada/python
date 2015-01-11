import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
#sys.path.append('/usr/lib64/python2.6/site-packages/')

from fabric.api import *
import MySQLdb
from time import localtime, strftime
import signal
import fcntl
import logging
from warnings import filterwarnings
import time

env.skip_bad_hosts=True
env.user="indigoadmin"
env.password="xxxxxxxx"

#Creating logger
logger=logging.getLogger(sys.argv[0])
logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO)
filterwarnings('ignore',category=MySQLdb.Warning)

#Creating a file handler for logging
loghandler=logging.FileHandler('panda.log')
#loghandler.setLevel(logging.INFO)

#Formatting
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
loghandler.setFormatter(formatter)

#Add the handlers to the logger
logger.addHandler(loghandler)

def query_product(n):
 myquery="select product, round(avg( 1000000*unix_timestamp(stop_time) + stop_time_ms - 1000000*unix_timestamp(start_time) - start_time_ms ) / 1000 ) as `Submission Time (ms)`, round(avg(blob_size)) as `Blob Size (Kb)`, count(parent.parent_id) as `count` from dcs_log, parent where dcs_log.parent_id = parent.parent_id and dcs_log.message = \"success\" and dcs_log.start_time > date_sub(UTC_TIMESTAMP(), interval %d hour) group by product;" % n
 return myquery

def query_site(n):
 myquery="select round(avg(1000000*unix_timestamp(stop_time) + stop_time_ms - 1000000*unix_timestamp(start_time) - start_time_ms ) / 1000 ) as `Submission Time (ms)`, round(avg(blob_size)) as `Blob Size (Kb)`, count(parent.parent_id) as `count` from dcs_log, parent where dcs_log.parent_id = parent.parent_id and dcs_log.message = \"success\" and dcs_log.start_time > date_sub(UTC_TIMESTAMP(),interval %d hour);" % n
 return myquery

def timeouthandler(signum,frame):
 logger.info("Timeout. Task could not be completed in less that 3 min. Exiting...")
 sys.exit(1)

signal.signal(signal.SIGALRM,timeouthandler)

#First result: By product
def parsingbyproduct(results):
 byproduct={}
 for value in results.values():
  if type(value).__name__ == '_AttributeString':
   x=value.split('\n')
   x.pop(0)
   for i in x:
    i=i.strip('\r')
    i=i.split('\t')
    i.append(1)
    if i[0] in byproduct:
     byproduct[i[0]]=[int(k)+int(v) for k,v in zip(byproduct[i[0]],i[1:5])]
    else:
     byproduct[i[0]]=i[1:5]
 return byproduct

#Second result: By site
def parsingbyhost(results):
 byhost={}
 for host in results:
  if type(results[host]).__name__ == '_AttributeString':
   x=results[host].split('\n')
   x.pop(0)
   if not x: byhost[host[0:4].upper()]=[0,0,0,1]
   for stats in x:
    stats=stats.strip('\r')
    stats=stats.split('\t')
    stats=[0 if i == 'NULL' else int(i) for i in stats]
    stats.append(1)
    site=host[0:4].upper()
    if site in byhost:
     byhost[site]=[k+v for k,v in zip(byhost[site],stats)]
    else:
     byhost[site]=stats
  else: byhost[host[0:4].upper()]=[0,0,0,1]
 return byhost

def parsinghostproduct(results):
 byhostproduct={}
 for host in results:
  if type(results[host]).__name__ == '_AttributeString':
   x=results[host].split('\n')
   x.pop(0)
   for i in x:
    i=i.strip('\r')
    i=i.split('\t')
    if host in byhostproduct:
     byhostproduct[host].append(i[0])
    else:
     byhostproduct[host]=[i[0]]
 return byhostproduct

def injectdatahostproduct(parsedata,connection,table):
 logger.info("Injecting data on table %s" % table)
 inserts={}
 for host in sorted(parsedata):
  prodlist=parsedata[host]
  nproduct=len(prodlist)+1
  prodfields=','.join(["product"+str(i) for i in xrange(1,nproduct)])
  values=','.join(['%s']*nproduct)
  values="VALUES (%s)" % values
  queryinsert="INSERT INTO %s(host,%s) %s" % (table,prodfields,values)
  data=[host]
  for i in prodlist: data.append(i)
  data=tuple(data)

  if queryinsert in inserts:
   inserts[queryinsert].append(data)
  else:
   inserts[queryinsert]=[data]

 with connection:
  cursor=connection.cursor()
  cursor.execute("DELETE FROM %s" % table)
  for ins in inserts:
   cursor.executemany(ins,inserts[ins])
  connection.commit()


def injectdatahostproduct_v2(parsedata,connection,table):
 logger.info("Injecting data on table %s" % table)
 data=[]
 values="VALUES (%s,%s)"
 queryinsert="INSERT INTO %s(host,product) %s" % (table,values)
 for host in sorted(parsedata):
  prodlist=",".join(parsedata[host])
  data.append((host,prodlist))

 with connection:
  cursor=connection.cursor()
  cursor.execute("DELETE FROM %s" % table)
  cursor.executemany(queryinsert,data)
  connection.commit()

#Injecting data into MySQL DB
def injectdata(parsedata,connection,table,column):
 logger.info("Injecting data on table %s" % table)
 data=[]
 values="VALUES (%s,%s,%s,%s)"
 queryinsert="INSERT INTO %s(%s,blobsize,avgsubtime,num_acorns) %s " % (table,column,values)
 for x in sorted(parsedata):
  n=parsedata[x][-1]
  avg_subtime=float(parsedata[x][0])/n
  avg_blobsize=float(parsedata[x][1])/n
  count_acorn=int(parsedata[x][2])
  data.append((x,avg_blobsize,avg_subtime,count_acorn))

 with connection:
  cursor=connection.cursor()
  cursor.execute("DELETE FROM %s" % table)
  cursor.executemany(queryinsert,data)
  connection.commit()

def LockFile(lock):
 try:
  fcntl.lockf(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
 except IOError:
  logger.info("Not able to obtain lock. Script already running.")
  sys.exit(1)

def UnlockFile(lock):
 fcntl.lockf(lock, fcntl.LOCK_UN)

def set_hosts():
 ac='active_hosts.txt'
 f=open(ac).readlines()
 for host in f:
  host=host.strip()
  if host[0] != "#":
   env.hosts.append(host)

@parallel(pool_size=40)
def query_hosts(nquery,query):
 logger.debug("%s: %s" % (nquery,env.host_string))
 command='/usr/bin/mysql -udcs -pdcs -D data_collection -se \'%s\'' % query
 return run(command,warn_only=True)

results={}
set_hosts()

#result_queries=['query1','query2','query3']
result_queries=['query1','query2','query3','query4','query5']
inject_queries=['query1','query2','query3','query4']
#inject_queries=['query1']
queries={
          'query1':[query_product(24),parsingbyproduct,"product_stats","product"],
          'query2':[query_site(24),parsingbyhost,"site_stats","site"],
          'query3':[query_product(1),parsingbyproduct,"product_stats_hourly","product"],
          'query4':[query_site(1),parsingbyhost,"site_stats_hourly","site"],
          'query5':[query_product(120),parsinghostproduct,"host_product"],
        }

time1=strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
logger.info("Start of cronjob at %s." % time1)
lock=open(".pandalock",'w')

#Script will timeout after 3 min.
signal.alarm(300)
#Grabbing the lock
LockFile(lock)
timepoch1=time.time()
with hide('output','running','warnings'), settings(warn_only=True,quiet=True):
 for query in result_queries:
  logger.info("Running %s ..." % query)
  qtime1=time.time()
  results[query]=execute(query_hosts,query,queries[query][0])
  qtime2=time.time()
  logger.info("Elapsed time for %s is %.2f secs." % (query,qtime2-qtime1))

time2=strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
logger.info("Finish running queries on Panda DCS at %s" % time2)
#print "-" * 70
#
#Initiate connection to MysqlDB
host='17.106.150.149'
database='panda_stats'
user='panda_stats'
passwddb='panda'

logger.info("Initiating connection to Mysql DB for data injection")
try:
 connection=MySQLdb.connect(host=host,user=user,passwd=passwddb,db=database)
except MySQLdb.Error as e:
 logger.info("Error %d: %s" % (e.args[0],e.args[1]))
 sys.exit(1)

#for query in queries:
for query in inject_queries:
 table=queries[query][2]
 column=queries[query][3]
 injectdata(queries[query][1](results[query]),connection,table,column)

injectdatahostproduct_v2(parsinghostproduct(results['query5']),connection,'host_product_v2')

time3=strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
logger.info("End of cronjob at %s" % time3)
connection.close()
timepoch2=time.time()
logger.info("Total time elapsed for this cronjob: %.2f secs" % (timepoch2-timepoch1))
UnlockFile(lock)
#Resetting alarm
signal.alarm(0)
