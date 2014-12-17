#!/usr/bin/python

def mysquare(x):
 return x**2

def mycube(x):
 return x**3


funcs=[mysquare,mycube]

print map(lambda x:x(2),funcs)
print dir(mysquare)


print mysquare.func_name
