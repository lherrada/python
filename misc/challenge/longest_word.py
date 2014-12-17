#!/usr/bin/python
#Exercise 1: Find longest word

import re

file1='alice.txt'
myfile=open(file1)
maxword=''
maxlen=0

for i in myfile:
 i=i.strip('\n')
 list1=re.split('\s+',i)
 list1=sorted(list1,key=len,reverse=True)
 print list1[0],maxlen
 if len(list1[0])>maxlen:
  maxlen=len(list1[0])
  maxword=list1[0]
 
print "===>", maxword
