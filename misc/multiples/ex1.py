#!/usr/bin/python

A=[0 for _ in xrange(35)]

i=3
while i < len(A):
 A[i]=1
 i+=3

i=4
while i < len(A):
 A[i]+=2
 i+=4

print A

for i in A:
 if i == 3:
  print "Linkedin"
 elif i == 1:
  print "Link"
 elif i == 2:
  print "Edin"
 else:
  print "------"  

mask=[0, 1, 2, 0, 1, 0, 2, 1, 0, 0, 3, 0]
