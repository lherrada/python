#using the generator pattern (an iterable)





class firstn(object):
 def __init__(self,n):
  self.n=n
  self.num ,self.nums = 0, []

 def __iter__(self):
  return self
 
 def next(self):
  if self.num < self.n:
   cur,self.num = self.num,self.num + 1
   return cur
  else:
   raise StopIteration()

if __name__ == '__main__':

 a=firstn(10) 
 print a.__dict__

total=sum(firstn(100))
print total

total=sum(a)
print total


'''
 p=iter(a)
 print next(p)
 print next(p)


 for i in a:
  print i

print "-" * 20
print sum(a)
'''
