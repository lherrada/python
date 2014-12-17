#!/usr/bin/python

#Another solution for this problem:
#echo "minute, number_of_messages";cat message.log |awk '{print $1,$2,$3}'|awk -F: '{OFS=":";print $1,$2}'|uniq -c|perl -pe 's/^\s+(\d+)\s+(.*)/$2,$1/'


import re


myhash={}

try:
 myfile=open("message.log")
except IOError as e:
 print e.strerr

for line in myfile:
 line=line.strip()
 line=re.split(":",line)
 line=":".join(line[0:2])
 
 if line in myhash:
  myhash[line]+=1 
 else:
  myhash[line]=0
  myhash[line]+=1 

print "minute, number_of_messages"

for key in sorted(myhash):
 print key + "," + str(myhash[key])

 
