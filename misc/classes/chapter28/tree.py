#!/usr/bin/python

class A(object):pass
class B(A):pass
class C(object): pass
class D(B,C): pass
class E(D): pass

def classtree(xclass,npoints):
 print "." * npoints + xclass.__name__ 
 for i in xclass.__bases__:
  classtree(i,npoints + 3) 

x=E()
#print x.__class__
#print x.__class__.__bases__

classtree(x.__class__,3)



