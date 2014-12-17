#!/usr/bin/python
import random

def insert(array,val):
 N=len(array)
 for i in xrange(N):
  if val < array[i]:
   array.insert(i,val)
   return
 array.append(val)
 #array.insert(N,val)

#x=[3,17,11,42,82,91,12,34]
array=list()

for _ in xrange(20):
  array.append(random.randint(0,99))

print array

sortedarray=list()
for i in array:
 insert(sortedarray,i)
 
print sortedarray

