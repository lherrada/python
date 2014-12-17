def addone(myfunc,n):
 def square(m):
  return myfunc(n)**m
 return square

def oldfunc(n):
 return n

def superpower():
 dict1={}
 def power2(n): return n**2
 def power3(n): return n**3
 def power4(n): return n**4

 dict1['power2']=power2
 dict1['power3']=power3
 dict1['power4']=power4

 return dict1

if __name__ == '__main__':
 x=addone(oldfunc,5)  
 print x(2)
 print x(3)
 
 print '-' * 30
 
 y=superpower()
 #print y 
 for key in sorted(y.keys()):
  print y[key](5)
