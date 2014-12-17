#!/usr/bin/python
import os

def printdir(dir):
 filenames=os.listdir(dir)
 for i in filenames:
  print i
  print os.path.join(dir,i)
  print os.path.abspath(os.path.join(dir,i))
  print "-"*30

def dircreation(dir):
 if not os.path.exists(dir):
  os.mkdir(dir)
 else: print "Directory %s already exists" % (dir,)

#mydir="/home/lherrada/programming/python/begin"
#printdir(mydir)
#printdir(os.getcwd())

printdir('test/')
#printdir('../utilities/')

mypath='/root/utils/app1.py'

print os.path.dirname(mypath)
print os.path.basename(mypath)

#mypath='test'
#mypath='/home/lherrada/programming/python/'
mypath='test1'
dircreation(mypath)

