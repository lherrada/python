def decorate(func):
 print "Decorating the function: %s" % func.__name__
 def wrapped(*args,**kwargs):
  print "Invoking the wrapped function with args",args,kwargs
  return func(*args,**kwargs)
 print 'end'
 return wrapped
 
def test(*args,**kwargs):
 return sum(args) 

test=decorate(test)

#print type(test)

n=test(3,4,5,5,6,7,8,name='Luis')

print n



