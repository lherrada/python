#!/usr/bin/python

class Attrdisplay():
 def gatherattr(self):
  listattr=[]
  for i in self.__dict__: 
   listattr.append('%s: %s' % (i,getattr(self,i)))
  return ', '.join(listattr)

 def gatherattr2(self,obj):
  for i in obj.__dict__:
   print "%s --> %s" % (i,getattr(obj,i))


 def __str__(self):
  return "[%s] %s" % (self.__class__.__name__,self.gatherattr())
 

class Father(Attrdisplay):
 def __init__(self,name="Salvador"):
  self.name=name

class Son(Father):
 def __init__(self,lastname='Herrada'):
  Father.__init__(self)
  self.lastname=lastname

 def __str__(self):
  print "Calling __str__ from son class"
  return Attrdisplay.gatherattr(self)  

 def __getattr__(self,attrname):
  print "Getting value %s" % attrname 
  if attrname in ['age','country','company']:
   print "Attribute %s allowed but not set" % attrname
  else:
   raise AttributeError(attrname)

 def __setattr__(self,attrname,value):
  if attrname in ['age','country','company','name','lastname']:
   #self.attrname=value
   self.__dict__[attrname]=value
   print "Setting attribute %s to value %s" % (attrname,value)
  else:
   raise AttributeError(attrname + ' not allowed')

 def __repr__(self):
  return "Representing: %s" % self.lastname


if __name__ == '__main__':

 lhm=Son()
 lhm.country="Peru"
 
 print lhm
 print repr(lhm)

 #lhm.age=30
 #lhm.age

 #print lhm

