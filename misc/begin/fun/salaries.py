#!/usr/bin/python
import re

file1="salaries.txt"
try:
 myfile=open(file1);
except IOError as e:
 print "I/O error[{0}]: {1}".format(e.errno,e.strerror)

mydict={}

for line in myfile:
 line=line.strip()
 mylist=re.split("\s+",line)   
 mydict[mylist[0]]=mylist[1]

print mydict

for key,value in sorted(mydict.iteritems(),key=lambda (k,v):(v,k),reverse=True):
 print "%s: %d" % (key,int(value))
 

