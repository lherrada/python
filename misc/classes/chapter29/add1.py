class member():
 def __init__(self,value):
  self.value=value
  
 def __add__(self,other):
  print "Sum of",self.value,"and",other
  return (self.value + other) 

 def __radd__(self,other):
  print "RSum of",self.value,"and",other 
  return (self.value + other)

if __name__ == '__main__':
 n1=member(20)
 n2=member(80)

 print n1 + 30
 print 100 + n1

 print "-" * 40 
 print n1 + n2

 print "-" * 40 
 print n1+20+n2+n1+5
