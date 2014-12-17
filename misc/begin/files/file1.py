#!/usr/bin/python
import sys,re

#myfile='mytext.txt'
myfile='alice.txt'

try:
 data=open(myfile).read()
except IOError as e:
 print "I/O error({0}): {1}".format(e.errno,e.strerror)
 sys.exit(1)

mydict={}

for line in data.split('\n'):
 for word in re.split('\s+',line):
  match=re.search('^(\W*)(.*?)(\W*)$',word)
  word2=match.group(2).lower() 
  if re.search('\w+',word2):	
   if word2 in mydict.keys(): 
    mydict[word2]+=1
   else:
    mydict[word2]=0
    mydict[word2]+=1    

dict2={}

for (k,v) in sorted(mydict.iteritems(),key=lambda (k,v):(v,k),reverse=True):
 if v not in dict2:
  dict2[v]=[]
  dict2[v].append(k)
 else:
  dict2[v].append(k)
  
for i in sorted(dict2,reverse=True):
 dict2[i].sort()
 print "%d: %s" % (i,dict2[i])
