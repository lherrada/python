#!/usr/bin/python

"""
Fibonacci numbers:
F(n)=F(n-1) + F(n-2)
with F(0)=0 and F(1)=1
"""

#Iterative solution

def fib0(n):
 if n == 0:
  return 0
 elif n == 1:
  return 1
 else:
  F=[]
  F[0:2]=0,1
  for i in range(2,n+1):
   f=F[i-1]+F[i-2]
   F.append(f)
 return f

def fib1(n):
 a,b=0,1
 for i in range(n):
  a,b=b,a+b 
 return a

#Recursive Solution

def fib2(n):
 if n == 0 :
    return 0
 elif n == 1:
    return 1
 else:
  return fib2(n-1)+ fib2(n-2)

fibohash={}
fibohash={0:0,1:1}

def fib3(n):

 if not n in fibohash:
  fibohash[n]=fib3(n-1) + fib3(n-2) 
 return fibohash[n]
  


if __name__ == '__main__':
 import timeit

 
 for i in range(1,50):
  s="fib0("+str(i)+")" 
  time1=timeit.timeit(s,setup="from __main__ import fib0")

  s="fib1("+str(i)+")" 
  time2=timeit.timeit(s,setup="from __main__ import fib1")

  s="fib3("+str(i)+")" 
  time3=timeit.timeit(s,setup="from __main__ import fib3")

  print "n=%d,\tfib0: %7.6f\tfib1: %7.6f\tfib3: %7.6f\n" % (i,time1,time2,time3),


#t1=timeit.Timer("fib0(2)")
#time1=t1.timeit(3)


#print "Fib1(10) is %7.6f" % timeit.timeit('fib1(10)',number=1)


#n=1500
#print "Iterativo (LHM) -----> ",fib0(n)
#print "Iterativo       -----> ",fib1(n)
#print "Recursivo -----> ",fib2(n)
