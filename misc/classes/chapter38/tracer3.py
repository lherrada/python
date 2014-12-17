calls=0

def tracer(func):
 def wrapper(*args,**kwargs):
 # print 'ARGS:',args
 # print 'KWARGS:',kwargs
  global calls
  calls +=1
  print('call %s to %s' % (calls,func.__name__))
  return func(*args,**kwargs)
 return wrapper

@tracer
def eggs(x,z):
 print (x**z)

@tracer
def spam(x,y):
 print (x+y)

if __name__ == '__main__':

 eggs(2,3)
 eggs(3,z=4)

 print '-' * 20 
 spam(10,20)
 spam(x=9,y=23)
 print "CALLS:",calls
