#!/usr/bin/python

age=37
x,y=10,20

def f1():
 print age
 print "--> " + str(x)
 global z
 z=100 
 print "--> " + str(z)

def f2():
 print "from f2() --> " + str(z) 
 
f1()
f2()
