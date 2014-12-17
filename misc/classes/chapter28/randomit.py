import random

class myrandom():
 def __init__(self,n):
  random.seed()
  self.n=n
  self.count=0  

 def __iter__(self):
  return self

 def next(self):
  if self.count < self.n: 
   myrandom=10*random.random()
  else:
   raise StopIteration
  self.count+=1
  return myrandom

if __name__ == '__main__':
 #lhm=myrandom(5) 
 for i in myrandom(10): 
  print "%2.3f" % i 
