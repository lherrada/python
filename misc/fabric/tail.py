#!/usr/bin/python
import os

#myfile='brothers.txt'
myfile='alice.txt'
size=os.stat(myfile).st_size
nlines=10
counter=0

#print "SIZE: %s" % size

with open(myfile) as f:
 f.seek(size,0)
 while counter<nlines:
  if f.tell() == 1: break
 # print f.tell()
  f.seek(-2,1)
  if f.read(1) == '\n':
   counter+=1

 f.seek(-1,1)
 print f.read(),

