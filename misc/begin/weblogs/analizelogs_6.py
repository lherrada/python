#!/usr/bin/python

import re
# Script that finds out which is the number of request per
## combination of (source address,URL)

#From there you can find out what is the source with the highest number of request

def dumper(myhash):
 for k,v in myhash.iteritems():
  print "{0}: {1}".format(k,v)

#logs=open('NASA_access_log_Jul95')
logs=open('nasa.log')

myhash={}
myhost={}
j=0
for line in logs:
 line=line.strip('\n')
 #print len(re.split('\s+',line))
 
# mylist=re.split('\s+',line)
# lookup=re.split('\s+',line)
 lookup=re.search(r'^(.*?)\s+(.*)"(GET)?\s+(.*?)\s+(.*?)\s+(\d+)',line)

 try:
  host=lookup.group(1)
#  host=lookup[0]
  website=lookup.group(4)
  errorcode=lookup.group(6)
 except AttributeError:
  pass

 tuple1=(host,website)

# print "{0} : {1} : {2}".format(host,website,errorcode)
 if host in myhost:
  myhost[host]+=1
 else:
  myhost[host]=0
  myhost[host]+=1
 
 if tuple1 in myhash:
  myhash[tuple1]+=1
 else:
  myhash[tuple1]=0
  myhash[tuple1]+=1

#dumper(myhash)
U=0
topip=[]
for key in sorted(myhost,key=myhost.__getitem__,reverse=True):
 topip.append(key)
 #print "{0}: {1}".format(key,myhost[key]) 
 U+=1
 if U == 10: break
#print topip
#print "="*30


for ip in topip:
 tuple1=[]
 U=0
 for k,v in myhash:
  if k == ip:
   tuple1.append((k,v,myhash[(k,v)]))
 for i in sorted(tuple1,key=lambda x: x[2],reverse=True):
  U+=1 
  print i  
  if U == 5: break


#print topip

#for key in sorted(myhash,key=myhash.__getitem__,reverse=True):


# print "{0}: {1}".format(key,myhash[key]) 
