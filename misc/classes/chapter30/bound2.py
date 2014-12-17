def square(n):
 return n**2

class C1:
 def __init__(self,value):
  self.value=value
 
 def __call__(self,args):
  return self.value + args

class C2:
 def __init__(self,value):
  self.value=value
 
 def method(self,n):
  return self.value * n

class Negation:
 def __init__(self,value):
  self.value=-2*value
 def __repr__(self):
  return str(self.value)

if __name__ == '__main__':
 
 c1=C1(1) 
 c2=C2(2)

 lista=[square,c1,c2.method,Negation]

 for i in lista:
  print i(5)

