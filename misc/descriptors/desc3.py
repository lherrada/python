#!/usr/bin/python

class GetOnlyDesc(object):
 
 def __get__(self,obj,classtype=None):
  print "__get__ method"
  pass

class C(object):
 d=GetOnlyDesc()


cobj=C()
x=cobj.d

cobj.d="Setting value"
print cobj.__dict__
 
x=cobj.d

