#!/usr/bin/python
import random

class Indexer:
 data=range(0,10)

 def __getitem__(self,index):
  print "getitem: ",index 
  return self.data[index]
  #return index*3
  #return "-> %d" % self.data[index] 

 def __setitem__(self,index,value):
  #print "Assigning value %d to data[%d]" % (value,index)  
  print "Index:",index,"Value:",value
  self.data[index]=value

X=Indexer()

random.seed()
#Assinging random values to X[i]
#for i in range(0,9):
# X[i]=int(10*random.random()) 

#for i in range(0,9):
# print X[i]

#Assigning values to only an slice
print "-" * 30
X=Indexer()
#X[0:5]=range(0,5)
X[0:5]=[25 for i in range(0,5)]
X[6]=20

for i in range(0,10):
 print X[i]

print "-" * 30
#The "in" operator causes the __getitem__ to be triggered
print "Testing in operator"
a=20
if a in X: print "Value %d found" % a

print "-" * 30
print "MAP"
print map(lambda x: x**2,X)

print "-" * 30
print "List Comprenhension"
#print [i**2 for i in X]

print "-" * 30
print "Sequence Assigments"
#(a,b,c,d)=X[3,6,8,9]
L=(a,b,c,d,e)=X[2:7]
print L 
