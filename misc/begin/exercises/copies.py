#!/usr/bin/python

A=['a','b','c']

print id(A)
#B=A[:]
B=A
print id(B)
B[0]='H'
print B
print id(B)
print A

C=['d','e',A,'z']
print C
A.append('J')
print C

print "=" * 40

dict1={'name':'Luis','age':37,'country':'Peru'}
#print dict1

dict2=dict1.copy()
dict2['name']='Silvia'
print dict1
print dict2
