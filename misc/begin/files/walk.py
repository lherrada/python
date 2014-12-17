#!/usr/bin/python
import os

mypath="/home/lherrada/programming/python/begin/classes"

for root,dirs,files in os.walk(mypath,topdown=False):
#for root,dirs,files in os.walk(mypath,topdown=True):
 for name in files:
  print os.path.join(root,name)
 
 for name in dirs:
  print os.path.join(root,name) 
 
 
 

# print root
# print dirs
# print files
# print "-" * 30





