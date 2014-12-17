#!/usr/bin/python

def map1(x):
 return "A" + str(x)

list1=[6,4,1,3]
print list(map(map1,list1))

print "="* 20
print map(lambda x: x**2,list1) 
 

