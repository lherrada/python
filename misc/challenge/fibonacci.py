#!/usr/bin/python
def fibonacci(n):
 if n == 0:
  return 0
 elif n == 1:
  return 1
 else:
  fibo=fibonacci(n-1) + fibonacci(n-2)
  return fibo

fibohash={}
fibohash={0:0,1:1}
def fibonacci2(n):

 if not n in fibohash:
  fibohash[n]=fibonacci2(n-1) + fibonacci2(n-2) 
 return fibohash[n]



n=int(raw_input("Type your number: "))

#for i in range(0,n):
# print "Fibonacci[%d] = %d" % (i,fibonacci(i))
 
for i in range(0,n):
 print "Fibonacci[%d] = %d" % (i,fibonacci2(i))

