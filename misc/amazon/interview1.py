#!/usr/bin/python3.1
import random

x= { random.randint(0,100) for _ in range(1,20) }
def randomgen():
 for i in x:
  yield i


def exercise1():
 return { i:None for i in randomgen() }
# for x in randomgen():
#  print(x) 
   
#print(exercise1())
print(exercise1())


def exercise2():
 h={}
 for i in randomgen():
  h[i]=None  
 return h

#print(exercise2())

def exercise3():
 return { i:None for i in randomgen() } 

#print(exercise3())
