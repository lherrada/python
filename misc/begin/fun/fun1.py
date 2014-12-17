#!/usr/bin/python

myfile="list.txt"

try:
 file=open(myfile);
except IOError as e:
 print "I/O error({0}): {1}.".format(e.errno,e.strerror); 
 exit(e.errno)

for i in file:
 print i,


