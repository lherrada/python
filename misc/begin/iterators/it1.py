#!/usr/bin/python

class myseq:

 fibohash={}
 fibohash={0:0,1:1}

 def myfunc(self,n):
  return 2 ** n 

 def __init__(self,nstop):
  self.x=-1
  self.nstop=nstop

 def next(self):
  self.x += 1
  if self.x >self.nstop:
   raise StopIteration
  #return 2 ** self.x
  return self.fibonacci(self.x) 
  
 def __iter__(self):
  return self

 def fibonacci(self,n):
  if not n in myseq.fibohash:
   myseq.fibohash[n]=self.fibonacci(n-1) + self.fibonacci(n-2)
  return myseq.fibohash[n]
  

s = myseq(40)
for i in s:
 print "---> ",i

#it=iter(myseq(10))
#print next(it)
#print next(it)
#print next(it)

#print "=" * 20

"""
n=0
for i in s:
 n+=1
 if n>10: break
 print "Next number: %d" % i

print "=" * 10
"""
 



