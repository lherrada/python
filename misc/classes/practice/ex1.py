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
#class Father(object):
 def __init__(self,name="Salvador"):
  self.name=name

#class son(father,attrdisplay):
class Son(Father):
 def __init__(self,lastname):
  Father.__init__(self)
  self.lastname=lastname

 def __str__(self):
  print "Calling __str__ from son class"
  return Attrdisplay.gatherattr(self)  

 def __getattr__(self,attrname):
  return "Getting value: %s -> %s" % (attrname,self.__dict__[attrname]) 


if __name__ == '__main__':
 lhm=Son('herrada')
 lhm.country="Canada"
 #print lhm.copine
 #getattr(lhm,copine)

 print lhm.__getattr__('country') 
 print getattr(lhm,'country')

# p=Attrdisplay()
# p.gatherattr()
 
 print lhm

