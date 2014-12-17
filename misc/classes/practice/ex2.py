def f(obj,index):
 return obj[index-1]


class A:
 def __init__(self,a):
  self.a=a
 
 def __getitem__(self,index):
  if index.__class__.__name__ == 'int':
   index=index-1
  elif index.__class__.__name__ == 'slice':
   index=slice(index.start-1,index.stop-1)
  return self.a[index]

a=range(1,11)
a=A(a)
print a[1]
print a[9]
