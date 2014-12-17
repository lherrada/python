#!/usr/bin/python

x=100

def f():
 global x 
 x+=120


print x
f()
print x
