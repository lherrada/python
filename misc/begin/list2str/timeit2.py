#!/usr/bin/python
import time

def timing(f,n,m):
 print f.__name__
 r=range(0,n)
 t1=time.clock()
 for i in r:
  f3(m)  
 t2=time.clock()
 print "Time elapsed: %7.6f" % round(t2-t1,3)

def f3(list):
 string = " "
 for char in map(chr,list):
  string=string + ' ' + char
 return string

list1=range(0,255)

timing(f3,100000,list1)
