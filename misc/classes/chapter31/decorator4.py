class LHM:
 counter=0
 def __init__(self,func):
  self.func=func

 def __call__(self,*args):
  self.counter+=1
  print "Calling %s for %s time(s)" % (self.func.__name__,self.counter)
  self.func(*args)


@LHM #dataprinting=LHM(dataprinting)
def dataprinting(*args):
 for i in args:
  print "DATA -->",i

if __name__ == '__main__':
 dataprinting("Herrada","Mateo")
 dataprinting("Canada","USA")
 dataprinting()

 print "-" * 30
 print dataprinting.__dict__
 dataprinting.func("Luis")
 print dataprinting.counter

 print "-" * 20
 print LHM 
 print type(LHM) 
 LHM.id=10808122
 print LHM.__dict__
 print LHM.counter
