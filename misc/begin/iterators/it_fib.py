#!/usr/bin/python

import sys

class seq_fib:
 
 fibohash={}
 fibohash={0:0,1:1}

 def fib1(self,n):
  if not n in seq_fib.fibohash:
   seq_fib.fibohash[n]=self.fib1(n-1) + self.fib1(n-2)
  return seq_fib.fibohash[n]

 def __init__(self,n):
  self.x=-1
  self.n=n

 def next(self):
  self.x+=1
  if self.x > self.n:
   raise StopIteration 
  return self.fib1(self.x)

 def __iter__(self):
  return self  

s=seq_fib(50)
print sys.getsizeof(s)

for i in s:
print i

#print s

#for i in s:
 #print i

#gen=(i for i in s)

#for i in gen:
# print i


