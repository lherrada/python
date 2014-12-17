class member():
 def __init__(self,value):
  self.value=value
  
 def __add__(self,other):
  if isinstance(other,member):
   other=other.value  

  print "Sum of",self.value,"and",other
  return member(self.value + other) 

 def __radd__(self,other):
  print "RSum of",self.value,"and",other 
  return member(self.value + other)

 def __str__(self):
  return "member: %s" % self.value

 def __iadd__(self,other):
  print "Call to __iadd__:",self.value,"and",other
  self.value+=other
  return self

if __name__ == '__main__':
 n1=member(20)
 n2=member(80)
 print n1 + 30

 print "-" * 30
 print 120+n2 

 print "-" * 30
 print n1 + n2 

 print "-" * 30
 n3=member(n1)
 print n3
 
 print "-" * 30
 #print n1 + 2 + 2 + n2 + 1 
 n1+=36
 print n1

 print "-" * 30
 n4=member(10)
 n4+=1
 n4+=1
 print n4

 print "-" * 30
 n4+=n2 
 print n4
