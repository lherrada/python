#!/usr/bin/python
#Exercise 1: Find longest word

import re

file1='alice.txt'
myfile=open(file1)
maxword=''
maxlen=0

mydict1={}

for i in myfile:
 i=i.strip('\n')
 list1=list(i)
 for j in list1:
  if j in mydict1:
   mydict1[j]+=1
  else:
   mydict1[j]=0
   mydict1[j]+=1
 
vowels=['a','e','i','o','u']
numbers = [mydict1[i]  for i in vowels]

result=dict(zip(vowels,numbers)) 

for i in sorted(result,key=result.__getitem__,reverse=True):
 print "%s: %d" % (i,result[i])
