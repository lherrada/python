def f1(x=20):
 def f2(**pargs):
  print pargs
  print x
 return f2 

def f3(age=37,code=001):
 class A:
  def __init__(self,param1,param2):
   self.age=param1
   self.code=param2

 a=A(22,111)
 
 def f4(obj):
  print a.__dict__
  print type(obj)
 return f4

if __name__ == '__main__':
 myf1=f1(150) 
 myf1(name='Luis',lastname='Herrada')
 print "-" * 30
 myf3=f3(42,002)
 myf3([20,21,22])
