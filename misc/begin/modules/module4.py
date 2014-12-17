#!/usr/bin/python

#from small import x,y

#print x
import small
import sys
print id(small.x)
print small.x

small.x=100
print id(small.x)
print small.x
#print small.y
