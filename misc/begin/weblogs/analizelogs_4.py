#!/usr/bin/python
#The total number of request every minute


import re

def dumper(myhash):
 for k,v in myhash.iteritems():
  print "{0}: {1}".format(k,v)


logs=open('NASA_access_log_Jul95')

myhash={}
j=0
for line in logs:
 j+=1
 line=line.strip('\n')
 #print len(re.split('\s+',line))
 
 mylist=re.split('\s+',line)
 #print "--> %d" % j 
 #mydate=mylist[3].split(':')[:-1]
 mydate=mylist[3].split(':')[0]
 #mydate=':'.join(mydate)
 if mydate in myhash:
  myhash[mydate]+=1
 else:
  myhash[mydate]=0
  myhash[mydate]+=1

#dumper(myhash)

for key in sorted(myhash,key=myhash.__getitem__,reverse=True):
 print "{0}: {1}".format(key,myhash[key]) 



#myhash2={}

#for k,v in myhash.iteritems():
# print "%s: %d" % (k,v)
# if v in myhash2: 
#  myhash2[v]+=1
# else:
#  myhash2[v]=0
#  myhash2[v]+=1

#print myhash2

#myhash2={}
#for value in myhash.values():
# if value in myhash2: 
#  myhash2[value]+=1
# else:
#  myhash2[value]=0
#  myhash2[value]+=1
 
#print myhash2
