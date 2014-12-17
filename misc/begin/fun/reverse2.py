#!/usr/bin/python

import sys,re

filename="excerpt.txt"
try:
 myfile=open(filename)
except IOError as e:
 print "I/O Error[{0}]: {1}".format(e.errno,e.strerror)
 exit(1)


for line in myfile:
 line=line.strip();
 mylist=re.split("\s+",line) 
 mylist.reverse()
# print " ".join(mylist)

print "=" * 30

myfile=open(filename)

for line in myfile:
 line=line.strip()
 mylist=re.split("\s+",line)
# mylist2=map((lambda x:x[::-1]),mylist)
 mylist2=[x[::-1] for x in mylist]
 mylist2.reverse()
 #print " ".join(mylist2)

print "=" * 30

mydict={'Yahoo': 135,
	'Idanalytics': 105,
	'Google':150
	}	

print mydict.__getitem__('Yahoo')

for key,value in sorted(mydict.iteritems(),key=lambda k: k[1],reverse=True):
 #print "{0}:{1}".format(key,str(mydict[key]))
 print key,value 
 
#for k in mydict.iteritems():
 #print "%s: %d" % (k,v)
 #print type(k) 

