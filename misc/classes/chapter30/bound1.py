def square(args):
 return args**2

class Number:
 def __init__(self,base):
  self.base=base
  self.name="LHM"

 def double(self):
  return self.base * 2

 def triple(self):
  return self.base * 3

 def __call__(self,args):
  return "ARGS: %s" % args

# def __repr__(self):
 # return "%s: %s" % (self.__class__.__name__,self.base)

if __name__ == '__main__':
 x=Number(3)
 y=Number(4)
 z=Number(5)
  
 p=Number(10)
 print p("Luis")
 print "-" * 30
 
 obj=[x.double,y.double,z.double]

 for i in obj:
  print(i())

 bound=x.triple
 print dir(bound)

 print "-" * 30
 print bound()
  
 print bound.__self__
 print x
 print bound.__self__.name
 
 print bound.__func__
 print bound.__func__(x)
 print bound.__class__
