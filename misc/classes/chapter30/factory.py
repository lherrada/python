def factory(aclass,*args):
 return aclass(*args)

class Fprint:
 def doit(self,message): print message
 def __call__(self,args):
  return "ARGS: %s" %args

if __name__ == '__main__':
 obj1=factory(Fprint)

 obj1.doit("Herradita")
 print obj1('Laurita')

 obj2=factory(obj1,'Jazmin')
 print type(obj2)
 print obj2
