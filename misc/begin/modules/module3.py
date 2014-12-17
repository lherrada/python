#!/usr/bin/python

from small import x,y

print x
print y

def f1(x,y):
 x=5
 y[1]='Silvia'
 print "Inside f1: %s" % x

f1(x,y)

print x
print y

y[0]='Maria Luisa'

print"="*20

import small
print small.x

small.x=100
print small.x
print small.y

