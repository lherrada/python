#!/usr/bin/python

"""
This is a script that implements sequence
"""

class seq:
 "Mi first sequence"

 def __init__(self):
  self.x=1

 def next(self):
  self.x*=2
  return self.x

 def __iter__(self):
  return self


class seq2:
 "My second sequence"

 def __init__(self):
  self.x=0
 
 def next(self):
  self.x+=1
  if self.x > 10: raise StopIteration
  return self.x**2

 def __iter__(self):
  return self

myseq=seq()
n=0

print myseq.__doc__

for i in myseq:
 print i
 n+=1
 if n>5: break

#=======================
print "="*10

myseq=seq2()
n=0

for i in myseq:
 print i





