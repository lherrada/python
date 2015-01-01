#!/usr/bin/python
"""
Lets learn about list comprehensions!. You are given three integers X,
Y and Z denoting the dimensions of a Cuboid. You have to print a list 
of all possible coordinates on the three dimensional grid, such that
at any point the sum Xi + Yi + Zi is not equal to N. If X = 2, 
then possible values of Xi can be 0, 1 and 2. The same applies to Y and Z.
"""
"""
X=2
Y=1
Z=1
n=2
"""

X=int(raw_input("x: "))
Y=int(raw_input("y: "))
Z=int(raw_input("z: "))
n=int(raw_input("n: "))

"""
for x in range(X+1):
 for y in range(Y+1):
  for z in range(Z+1):
   if x+y+z != n:
    L=[x,y,z] 
    mylist.append(L) 

#print mylist
"""

mylist=[ [x,y,z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x+y+z != n]
print mylist
