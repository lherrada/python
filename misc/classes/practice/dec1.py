
def outer_decorator(name):
 def decorator(func):
  print "Decorating %s" % func.__name__
  def wrapper(a,b):
   return "%s says: %s" % (name,func(a**2,b**2))
  return wrapper
 return decorator 

def decorator(func):
  print "Decorating %s" % func.__name__
  def wrapper(a,b):
   return "%s says: %s" % ('Luis',func(a**2,b**2))
  return wrapper
 
#suma=f1('Luis')(suma)

@outer_decorator('Silvia')
def suma(a,b):
 return (a+b)

#suma=outer_decorator('Luis')(suma)

print suma(3,4)

print "-" * 30
@decorator
def mult(a,b): return a*b

print mult(3,4)
