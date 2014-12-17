#!/usr/bin/python

import subprocess
import re

command=['df','-h']

p=subprocess.Popen(command,stdout=subprocess.PIPE)

#print p
output,error=p.communicate()
output=output.rstrip('\n')
mylist=output.split('\n')

del mylist[0:2]

thres=10
for i in mylist:
 s=re.split('\s+',i)
 usage=s[4].rstrip('%') 
 if int(usage)<thres: 
  print "Mountpoint %s is OK" %s[5]
 else:
  print "Please check disk usage for %s" % s[5]

#print output,

