class Spam:
 numinstances = 0
 
 def count(cls): 
  cls.numinstances+=1

 def __init__(self):
  self.count() #passes self.__class__ to count
 count = classmethod(count)

class Sub(Spam):
 numinstances = 0
 def __init__(self):
  Spam.__init__(self)
  
class Other(Spam):
 numinstances = 0

if __name__ == '__main__':
 x=Spam()
 print  x.numinstances

 x,y,z=(Sub(),Sub(),Sub())
 print  x.numinstances
