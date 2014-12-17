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
  pass

 def __set__(self,obj,value):
  self.name=value
  #print type(obj)
  #print type(self)
  print "Setting something: %s " % self.name
  pass

 def __delete__(self,obj):
  print "Deleting object"
  del self.name 
  pass


class C(object):
 d=Desc("Luisito")
 a=-10

#print C.__dict__

cobj = C()


print cobj.__class__.__name__
print cobj.__class__.__dict__['d']
cobj.__class__.__dict__['d'].__get__(cobj,C)
cobj.d

print "=" * 40
print cobj.__class__.__dict__['a']
print cobj.a

cobj.a=20
print cobj.__class__.__dict__['a']
print cobj.a

print "=" * 60

#cobj.__dict__['d'] = "Saludos"
#mydesc=Desc()
#print type(mydesc)

x=cobj.d

cobj.__class__.__dict__['d'].__set__(cobj,"Erika de Herrada")
cobj.d
print cobj.__dict__
#cobj.d="Luis Alberto"
cobj.b="Luis"
#print cobj.__dict__

#x=cobj.d

#cobj.__dict__['d'] = "Donde estas Erika!!??"
cobj.d = "Donde estas Erika!!??"

del cobj.d

"""

cobj.d="Luis Alberto"
cobj.d
print "="*30
C.d="Setting from the class C"
print C.d
"""
#print dir(cobj) 

#print type(x)
#cobj.d="Hola Amigos"

#cobj.__dict__['d']="Greetings"
