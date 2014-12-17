#!/usr/bin/python
import random

def swap(a,b):
 a=a+b
 b=a-b
 a=a-b

def rremove(x):
 x.pop()


random.seed()
y=[]
for i in xrange(1,30):
 y.append(random.randint(0,99))


'''
x=range(0,10)
y=[]
while x:
 k=random.choice(x)
 y.append(k)
 x.remove(k) 
'''
print y
#Bubble sorting
#The algorithm works by comparing each item in the list with the item next to it, 
#and swapping them if required. In other words, the largest element has bubbled to 
#the top of the array. The algorithm repeats this process until it makes a pass all
#the way through the list without swapping any items.

swapped=True
while swapped:
 swapped=False
 for i in xrange(1,len(y)):
  if y[i-1] > y[i]:
   y[i-1]=y[i-1]+y[i]
   y[i]=y[i-1]-y[i]
   y[i-1]=y[i-1]-y[i]
   swapped=True



print y

#x=[3,4,5]
#x[0]=x[0]+x[1]
#x[1]=x[0]-x[1]
#x[0]=x[0]-x[1]
#rremove(x)
#print x
 
 
