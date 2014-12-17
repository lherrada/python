class Super:
 def method(self):
  print "This is Super method"

class Tools:
 def __method(self):
  print "This is Tools method"
 def other(self): self.__method() 
 
class Sub1(Tools): 
 def __init__(self):
  self.method='mymethod'

class Sub2(Tools,Super):
 def actions(self): self.method() 
  #Tools.method(self)
  #Super.method(self)
  #self._Super__method()


if __name__ == '__main__':
 I=Sub1() 

# I._Tools__method() 
 I.other()
 print dir(I)

 print '-' * 30
 
 J=Sub2()
 J.actions()
 


 
