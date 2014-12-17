#!/usr/bin/python
#This script presents a report number of fields: number of lines

import re

logs=open('NASA_access_log_Jul95')

myhash={}
j=0
for line in logs:
 j+=1
 line=line.strip('\n')
 #print len(re.split('\s+',line))
 mylist=re.split('\s+',line)
 myhash[mylist[0]]=len(mylist)
 myhash[j]=len(mylist)




myhash2={}

for k,v in myhash.iteritems():
# print "%s: %d" % (k,v)
 if v in myhash2: 
  myhash2[v]+=1
 else:
  myhash2[v]=0
  myhash2[v]+=1

#print myhash2

myhash2={}
for value in myhash.values():
 if value in myhash2: 
  myhash2[value]+=1
 else:
  myhash2[value]=0
  myhash2[value]+=1
 
print myhash2
