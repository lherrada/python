#!/usr/bin/python
import random

#Bucket sort works as follows:

#Set up an array of initially empty "buckets".
#Scatter: Go over the original array, putting each object in its bucket.
#Sort each non-empty bucket.
#Gather: Visit the buckets in order and put all elements back into the original array.
#-----------------------------------------------

#Insert number and sort the array which is already partially sorted
def insertandsort(array,val):
 N=len(array)
 for i in xrange(N):
  if val < array[i]:
   array.insert(i,val)
   return
 array.append(val)

#Generator of random numbers
def rgen(n,m):
 for i in xrange(n):
  num=random.randint(0,m)
  yield num

nbuckets=10
#Setting up an array of empty buckets
nodes=[[] for _ in xrange(nbuckets)]
maxvalue=99
nlength=50

#Placing each number on its bucket and within the bucket,
#placing number is a position that  make the whole array 
#sorted

for number in rgen(nlength,maxvalue):
 print number,
 index=number/nbuckets
 insertandsort(nodes[index],number)

#Putting buckets all together
print "\n"
result=[]
for x in nodes:
 result+=x

print result
