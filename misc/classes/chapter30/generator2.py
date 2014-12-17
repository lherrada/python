#This is a real generator

def firstn(n):
 num=0
 while num < n:
  yield num
  num +=1


if __name__ == '__main__':
 a=firstn(5)
 print a.__class__
 #print(dir(a)) 
 

 for i in a: print i

 print "-" * 30
 print sum(firstn(20))

# for i in firstn(20):
 # print i 
