#!/usr/bin/python

def firstn(n):
 num=0
 while num < n:
  yield num
  num+=1


x=firstn(20)
a=25

if a in x:
 print "YES" 
else:
 print "NOO" 
 
print type(x)

x=firstn(5)
for i in x:
 print i

print "-"*20

a=sum(firstn(1000000000))
print a


