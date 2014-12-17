#!/usr/bin/python

#mask=[3,0,0,1,2,0,1,0,2,1,0,0]

n=35
A=[0 for _ in xrange(n)]

i=0
while i<len(A):
 A[i]=1
 i+=5

i=0  
while i<len(A):
 A[i]+=2
 i+=7

#print A

message={3: "Linkedin",
	 2: "Edin",
	 1: "Link",
	 0: "-------"
	}

for i in xrange(1,50):
 res=i%n
 print i,message[A[res]] 

  
