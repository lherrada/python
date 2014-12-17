class tracer:
 def __init__(self,func):
  self.calls=0
  self.func=func
 
 def __call__(self,*args):
  self.calls+=1
  print 'Call %s to %s' % (self.calls,self.func.__name__)
  self.func(*args)

@tracer # Same as spam = tracer(spam)
def spam(*names):
 for i in names:
  print " --> ",i

if __name__ == '__main__':
 spam('Luis')
 spam('Juan','Vanessa','Camucha')
 spam('Erika','Sonia')
 
