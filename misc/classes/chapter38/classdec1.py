def decorator(cls):
 class Wrapper:
  def __init__(self,*args):
   self.wrapped=cls(*args)
  def __getattr__(self,name):
   print "From wrapper: __getattr__"
   return getattr(self.wrapped,name)

  #Modification de la function suma en la clase C
  def suma(self,x,y):
   print "Going through decorator.suma"
   a=getattr(self.wrapped,'suma')
   return (a(x**2,y**2)) 

  def mult(self,x,y):
   return x*y

 return Wrapper


class C:
 def __init__(self,x,y):
  self.attr = 'spam'
  
 def suma(self,x,y):
  return (x+y)

 def diff(self,x,y):
  return (x-y) 

C=decorator(C)

x=C(1,2)
print x.attr

print "-"*30
a=x.suma(3,4)
print "--> ",a

print "-"*30
print x.mult(5,6)

print "-"*30
print x.diff(3,5)
