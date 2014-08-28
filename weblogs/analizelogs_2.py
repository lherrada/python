#!/usr/bin/python

import re
# Script that finds out which is the number of total number of request per source address.
#From there you can find out what is the source with the highest number of request

def dumper(myhash):
 for k,v in myhash.iteritems():
  print "{0}: {1}".format(k,v)


#logs=open('NASA_access_log_Jul95')
logs=open('nasa.log')

myhash={}
j=0
for line in logs:
 line=line.strip('\n')
 
 mylist=re.split('\s+',line)
 
 if mylist[0] in myhash:
  myhash[mylist[0]]+=1
 else:
  myhash[mylist[0]]=0
  myhash[mylist[0]]+=1

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
