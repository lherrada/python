#!/usr/bin/python
import os

def brokenlink(entryname):
 if os.path.islink(entryname) and not os.path.exists(entryname):
  print "Broken Link: %s" % entryname
  return entryname  

#mypath="/home/lherrada/programming/python/begin/classes"
mypath="/home/lherrada/programming/python/begin"

#for root,dirs,files in os.walk(mypath,topdown=True):

for root,dirs,files in os.walk(mypath,topdown=False):
 for name in files:
  entryname=os.path.join(root,name)
  brokenlink(entryname)
    
 for name in dirs:
  entryname=os.path.join(root,name) 
  brokenlink(entryname) 
 
 

# print root
# print dirs
# print files
# print "-" * 30





