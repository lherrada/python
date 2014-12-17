#!/usr/bin/python

import re
# Script that finds out which is the number of request per URL 
#From there you can find out what is the source with the highest number of request

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

 if mylist[6] in myhash:
  myhash[mylist[6]]+=1
 else:
  myhash[mylist[6]]=0
  myhash[mylist[6]]+=1

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
