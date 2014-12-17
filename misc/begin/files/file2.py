#!/usr/bin/python
import sys,re

myfile="mytext.txt"
myfile="alice.txt"

try:
 data=open(myfile)
except IOError as e:
 print "IOError [%d]: %s" % (e.errno,e.strerror)
 sys.exit(1)

mydict={}

for line in data:
 line=line.strip() 
 for word in re.split('\s+',line):
  match=re.search('^(\W*)(.*?)(\W*)$',word)
  word2=match.group(2).lower()
 
  if re.search('\w+',word2):
   if word2 in mydict:
    mydict[word2]+=1 
   else:
    mydict[word2]=0
    mydict[word2]+=1 

#for i in mydict:
# print "%s: %s" % (i,mydict[i]) 

dict2={}
  
for key in sorted(mydict,key=mydict.__getitem__,reverse=True):
 if mydict[key] not in dict2:
  dict2[mydict[key]]=[]
  dict2[mydict[key]].append(key) 
 else:
  dict2[mydict[key]].append(key) 


for i in sorted(dict2,reverse=True):
 dict2[i].sort()
 print "%s: %s" % (i,dict2[i])
