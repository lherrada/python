#!/usr/bin/python
import sys 

#file='file1.txt'
if len(sys.argv) < 2:
 print "You need to provide filename"
 sys.exit(1) 

file1=sys.argv[1]

try:
 f=open(file1)
except IOError:
# print "Cannot open ",file 
 raise

for i in f:
 print i.strip()  

