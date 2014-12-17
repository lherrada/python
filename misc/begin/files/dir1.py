#!/usr/bin/python

import sys,getopt,os

def help():
 print "%s [-d|dir] <dirpath>" % sys.argv[0]
 sys.exit(1);

""" Luis Herrada
This example is to clarify usage of directory commands
"""
try:
 opts,args = getopt.getopt(sys.argv[1:],'d:h',['dir=','help'])

except getopt.GetoptError as err:
 print err
 help()

myhash=dict(opts)
#print myhash

for i in myhash:
 if i in ('-h','--help'):
  help()
 if i in ('-d','--dir'):
  #print myhash[i]  
  filenames=os.listdir(myhash[i]) 
  #print filenames
  for j in filenames:
   path=os.path.join(myhash[i],j)
   if os.path.isfile(path):
     #print "File: %s" % os.path.abspath(j) 
     print "File: %s" % j 
   elif os.path.isdir(path):
     print "Directory: %s" % os.path.abspath(j)
     
print os.getcwd()

#print " -->",dict(opts)


