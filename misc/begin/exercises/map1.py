#!/usr/bin/python

def f1(v):
 sum=0
 for i in v:
  sum+=i**2 
 return sum 

def f2(v):
  return v**3

x=[1,2,3,4]

y=[5,10,15]

print map(f2,x) 
print map(f2,y) 

z=[x]
print z

print map(f1,[x])
print f1(x) 

print "="*30
g1=lambda x: x**2+1
print map(g1,x)
