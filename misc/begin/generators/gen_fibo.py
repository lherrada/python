#!/usr/bin/python

# fib(0)=0, fib(1)=1;
# fib(n)=fib(n-1) + fib(n-2)

fibohash={0:0,1:1}

def fibonacci(n):
 if n not in fibohash:
  fibohash[n]=fibonacci(n-1) + fibonacci(n-2)
 yield fibohash[n]
 #return fibohash[n]

def fibonacci2(n):
 a,b=0,1
 for i in range(n):
  yield a
  a,b=b,a+b
 
it=fibonacci2(10)

for i in it:
 print i

#fibonacci(10)
#print next(fibonacci(10))


#it=fibonacci(10)

"""
for i in it:
print i
"""



