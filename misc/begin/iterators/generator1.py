#!/usr/bin/python

def mygen():
 x,y =1,2
 yield x,y
 x+=1;x**=2
 yield x,y

it=mygen()

while(True):
 try:
  print it.next()
 except StopIteration:
  print "Iteration finished now." 
  break
 

