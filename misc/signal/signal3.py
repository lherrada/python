#!/usr/bin/python

class Person:
 'Test class describing person'
 def __init__(self,name,lastname='Garcia'):
  self.name=name
  self.lastname=lastname
  
 def displayname(self):
  print "Name: %s" % self.name 

 def getlastname(self):
  return self.lastname 

 def __str__(self):
  return "__Str__ says you are a Person"
 
 def __repr__(self):
  return "My representative is myself" 
 

myperson=Person('Luis')

print myperson.__doc__

myperson.age=30
#print dir(myperson)
print "Age is : %d" % getattr(myperson,'age')

print getattr(myperson,'lastname')

func=getattr(myperson,'getlastname')  

print dir(func)

print "Lastname is %s" % func()
 
print myperson
#print str(myperson)

print repr(myperson)
