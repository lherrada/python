class Parent:
 parentAttr=200
 def __init__(self,addx):
  self.addx = addx+Parent.parentAttr

 def getaddx(self):
  return self.addx

 def setaddx(self,x):
   self.addx=x

 def getparentAttr(self):
  return Parent.parentAttr

 def setparentAttr(self,x):
  Parent.parentAttr=x
 
 def __str__(self):
  #return "Value of addx is: ",self.addx
  return "Value of addx is %s" % self.addx

class Child(Parent):
 def __init__(self,x):
  self.addx=x**2

 
 

