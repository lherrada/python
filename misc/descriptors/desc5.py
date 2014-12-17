#!/usr/bin/python

class Desc(object):
 "Second Example of description creation"
 def __init__(self,name='Erikita'):
  self.name=name
 
 def __get__(self,obj,classobj):
  #print type(self)
  #print type(obj)
  #print self.__dict__ 
  print "Getting something: %s" % self.name
  return self.name 

 def __set__(self,obj,value):
  self.name=value
  print "Setting something: %s " % self.name
  pass

 def __delete__(self,obj):
  print "Deleting object"
  del self.name 
  pass


class C(object):
 d=Desc()
 a=-10

class D(C):
 myd=50 


dobj=D()

#dobj.d=100

print type(dobj)
print dobj.d
print "=" * 40

cobj = C()
print cobj.__class__
print cobj.__class__.__dict__['d']
cobj.__class__.__dict__['d'].__get__(cobj,C)
cobj.d

print "=" * 40
print cobj.__class__.__dict__['a']
print cobj.a

cobj.a=20
print cobj.__class__.__dict__['a']
print cobj.a

print "=" * 40

