#!/usr/bin/python

class C(object):
 def f(self):
  return "f is a class"


cobj=C()
print type(cobj)

#print cobj.f()
cobj.f()

print C.__dict__['f'].__get__(cobj,C)()
print "=" * 20
#print dir(cobj)
#print cobj.__dict__

print C.__dict__['f'](cobj)
print "=" * 20

b=3

print cobj.f()

print C.f(cobj)

def another_f(): return "Another f"

cobj.f = another_f

print cobj.f()


