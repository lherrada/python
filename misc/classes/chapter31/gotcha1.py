class C1:
 def __str__(self):
  return "Using C1 __str__: %s" % self.__class__.__name__

 def __method(self):
  print "Inside C1: %s" % self.__class__

 def message(self):
  C1.__method(self) 
  self.__method()
  C3.__method(self)

class C2(C1):
 def __init__(self,name='Luis'):
  self.name=name

 def method(self):
  print "Inside C2"

class C3(C2,C1):pass


if __name__ == '__main__':
 x=C3()
 print x
 x.method()

 print "-" * 30
 y=C3()
 y.method()
 y.message()
