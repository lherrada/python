#!/usr/bin/python
import sys
import os

path=sys.path
print path
for i in path[0:]:
 print i
print "=" * 20

#print os.environ

#print os.getenv("HOME")

myhash={'name':'Luis'}
myhash.setdefault('age',37)
myhash.setdefault('name','Eliza')
print myhash

print sys.argv

