#!/usr/bin/python
import os
import sys,getopt

def isbrokenlink(entryname):
 if os.path.islink(entryname) and not os.path.exists(entryname):
  return True
 else:
  return False


def myhelp():
 print "Usage: "
 print "%s -p <path>" % sys.argv[0]

try:
 opts,args = getopt.getopt(sys.argv[1:],'p:',['path='])
 dir="/home/lherrada/programming/python/begin/files"
except getopt.GetoptError:
 myhelp()
 sys.exit(1)

dict1=dict(opts)
#print dict1

if not os.path.isdir(dict1['-p']):
 print "Path %s does not exist" % dict1['-p']
 
mytree=[]

for root,dirs,files in os.walk(dict1['-p'],topdown=False):
 for name in files:
  entryname=os.path.join(root,name)
  mytree.append(entryname)

 for name in dirs:
  entryname=os.path.join(root,name)
  mytree.append(entryname)
  
for broken in filter(isbrokenlink,mytree):
 print "Broken Link: %s" % broken 
 
