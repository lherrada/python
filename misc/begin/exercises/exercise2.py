#!/usr/bin/python

#Write an script that allows you to put as an option a file , then reads the file and put in
# dict the data in that file 

import sys,getopt
import re

#print sys.argv[1:]
def myhelp():
 print "Usage: "
 print "%s -i <inputfile> -o <outputfile>" % sys.argv[0] 
 
try:
 opts,args = getopt.getopt(sys.argv[1:],'i:o:v',['input=','output=','verbose'])
 
except getopt.GetoptError: 
 myhelp()
 sys.exit(1);

dict1=dict(opts)

mandatory=['-i','-o']

for i in mandatory:
 if i not in dict1.keys():
  print "Argument %s missing. It  must be provided." % i
  myhelp()
  sys.exit(1)

try:
 f1=open(dict1['-i'],'r')
 f2=open(dict1['-o'],'w')

except IOError as e:
 print "I/O error({0}): {1}".format(e.errno,e.strerror)
 raise

listA=[]
initphrase="Processing started ..."
print initphrase 
print "-" * len(initphrase)

for line in f1:
 # print line,
 listA.append(tuple(re.split('\s+',line)[:-1]))
 
for i in sorted(dict(listA).keys()):
 str=i + ' : ' + dict(listA)[i].upper() + '\n'
 print "%s" % str, 
 f2.write(str)
# print "%s: %s" % (i,dict(listA)[i].upper())

