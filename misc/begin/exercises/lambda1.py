#!/usr/bin/python

f=lambda a,b=3: a+b**2

print f(2)

L=[lambda x:x**2,lambda x:x**3,lambda x:x**4]

for f in L:
 print f(2)


