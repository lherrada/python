#!/usr/bin/python

class Parent:
 #def __init__(self):
  #print "Calling constructor for Parent"

 def method1(self):
  print "Method 1 coming from Parent"
 
 def method2(self):
  print "Method 2 coming from Parent"

 def __str__(self):
  return "I am %s" % self.__class__.__name__  

 def __repr__(self):
  return '<(%s)>' % (self.__class__.__name__)

 

class Child(Parent):

 def method1(self):
  print "Method 1 coming from Child"
