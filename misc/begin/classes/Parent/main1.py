#!/usr/bin/python

from Parent import *

father=Parent(300)

print "Attribure addx 1:",getattr(father,'addx')
print "Attribure addx 2:",father.getaddx()


father.setaddx(1500);
print "Attribure addx 2:",father.getaddx()

print father 

print "="*30
print "Children' time"

child=Child(9)

if issubclass(Child,Parent):
 print "child is subclass of father"

if isinstance(child,Parent):
 print "child is an instance of Parent"

print "Child addx is ",child.getaddx()

child.setaddx(20)
print "Child addx is ",child.getaddx()

child.setparentAttr(150)
print "ParentAttr from child is",child.getparentAttr()


