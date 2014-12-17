def tracer(func):
 def wrapper(*args):
  wrapper.calls+=1
  print 'call %s to %s' %(wrapper.calls,func.__name__)
  return func(*args)
 wrapper.calls=0
 return wrapper

@tracer
def spam(a,b,c): return (a+b+c)

if __name__ == '__main__':
 print spam(1,2,3) 
 print spam('a','b','c')
