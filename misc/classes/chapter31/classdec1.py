YELLOW='\033[93m'
RED='\033[95m'
GREEN='\033[92m'
NORMAL='\033[0m'

class Cacher(object):
 def __init__(self,func):
  self.func=func
 
 def __call__(self,**kwargs):
   msg1= '%s%s%s' % (GREEN,self.func(**kwargs),NORMAL)
   return msg1

@Cacher
def message(name,age):
 return "Name is %s. Age is %d" % (name,age)
 
#message=Cacher(message)

print message(name='Luis',age=37) 
