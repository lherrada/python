#!/usr/bin/python
import random

#Randomly generating an array of 20 integers whose values are between 0 abd 99
random.seed()
y=[]
for i in xrange(1,20):
 y.append(random.randint(0,99))

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

#y is the sorted array 
print y

