#!/usr/bin/python
import sys 

def squares(n):
 for i in range(n):
  yield i ** 2
  x=5
  yield i ** 2 + x	

def squares2(n):
 sq=[i**2 for i in range(0,n)]
 return sq

mygen=squares(200)
print sys.getsizeof(mygen) 
print next(mygen)
print next(mygen)
print next(mygen)

mygen2=squares2(200)
print sys.getsizeof(mygen2) 

#print list(mygen)

#for i in mygen:
# print i

#print next(mygen)
#print next(mygen)


print "=" * 20

#for i in squares2(3):
# print i
