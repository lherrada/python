#!/usr/bin/python
import random

#This is a particular implementation of bucket sorting
#where the number of buckets is equal to the size of 
#the array to sort
#For big numbers, this method is not practical due to
#memory limitations.

y=[]
for i in xrange(1,20):
 y.append(random.randint(0,99))

print y
z=[0 for _ in xrange(100)]
x=[0 for _ in xrange(100)]

for i in y:
 z[i]=i
 x[i]+=1

result=[]
for i in range(len(z)):
 for j in range(x[i]):
  result.append(i) 

print result

 
