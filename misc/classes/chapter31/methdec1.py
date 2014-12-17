class decorator1:
 def __init__(self,func):
  self.func=func
 def __call__(self,*args):
  print "From __call__: %s" % self.__class__.__name__
  return self.func('',*args)
  #return self.func(*args)

def decorator(func): 
 def wrapper(*args):
  print "Call from def decorator"
  return func(*args)
 return wrapper

@decorator
def message(msg):
 print msg

class C:
 @decorator1
 def method(self,x,y):
  return (x+y)

'''
method=decorator(method)

'''



#:wmessage=decorator(message)

if __name__ == '__main__':
 message("Luis Herrada")

 x=C()
 print x.method(2,3)
 #print x.method(2,3)
 #C.method(x,2,3) --> 

 #print C.method(2,4)
