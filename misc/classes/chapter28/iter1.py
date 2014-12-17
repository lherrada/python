#!/usr/bin/python
import mymodule

class myiter:

 def __init__(self,start,stop):
  self.value=start-1
  self.stop=stop

 def __iter__(self):
  print "Cheersss!!! "
  return self

 def next(self):
  if self.value == self.stop: 
   raise StopIteration
  else:
   self.value+=1
  return self.value ** 2   
 
print dir(mymodule)
print mymodule.__class__
print mymodule.__doc__
print mymodule.lhm

print "=" * 30

lhm=myiter(4,9)
iter1=iter(lhm)
#print dir(iter1)

print "lhm"
print lhm
print lhm.__dict__
print lhm.__class__
print next(lhm)

print "=" * 30
print iter1
print dir(iter1)
print iter1.__dict__
print iter1.__class__
print next(iter1)

print "=" * 30
print "Haciendo loops"

for i in myiter(1,7):
 print i

print "=" * 40
ioc=myiter(5,15)
for i in ioc:
 print i

for i in ioc:
 print i



 
