def dividedec(func):
 print "Decorating function %s:" % func.__name__
 def wrapper(a,b):
  a=float(a)
  b=float(b)
  return func(a,b)  
 return wrapper

def dividedec2(func):
 print "Decorating2 function %s:" % func.__name__
 def wrapper(a,b):
  a=float(a)
  #b=float(b)
  try:
   n=a/b  
  #except ZeroDivisionError:
  # raise Exception("Division by zero not allowed")
  except Exception as ex:
   print "Exception was thrown: ",ex
   return 'n/a'
  return "%.3f" % n 
 return wrapper

 
def dividedec3(func):
 print "Decorating3 function %s:" % func.__name__
 def wrapper(a,b):
  a=float(a)
  #b=float(b)
  try:
   return "%.3f" % func(a,b)  
  #except ZeroDivisionError:
  # raise Exception("Division by zero not allowed")
  except Exception as ex:
   print "Exception was thrown: ",ex
   return 'n/a'
 return wrapper


 
 #return "%.3f" % (float(a)/float(b)) 
#divide=dividedec(divide)
@dividedec3
def divide(a,b):
 return (a/b)


print divide(12,6)
