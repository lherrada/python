#!/usr/bin/python
"""
Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?
"""

def mymax(x,y):
 if x>y:
  return x
 else: 
  return y

def max_in_list(mylist):
 return reduce(lambda x,y:x if x>y else y ,mylist) 


a=[3,4098,23,12,32,21,32,5,986,2000,434,2132,43]

b=[1,2,3,4,5]

#print reduce(lambda x,y: mymax(x,y),a) 
#print reduce(mymax,a)

print max_in_list(a)


