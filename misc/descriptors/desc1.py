#!/usr/bin/python

class mydescriptor(object):
 "This is my first descriptor example"

 def __init__(self,value):
  self.value=value

 def __get__(self,obj,objtype=None):
  pass
 # print dir(self)
 # print obj.__dict__
 # print objtype
  print "Retrieving value: ",self.value
#  return self.value 

 def __set__(self,obj,val):
  print "Setting value to ",val
  self.value=val
  #pass
 
 def __delete__(self,obj):
  print "Deleting"
  pass

class C(object):
 d=mydescriptor("Herrada")

cobj=C()
cobj.country='Canada'
#print mydescriptor.__doc__

print cobj.d

#result=cobj.d
#print result
#cobj.d = "Martinez"
#cobj.d
