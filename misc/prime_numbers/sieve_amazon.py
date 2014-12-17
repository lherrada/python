#!/usr/bin/python

def eras_sieve_v1(n):
 #A=[0 for i in range(0,n)]
 A=[0]*n
 i=2
 while i<n:
  if A[i]==0:
 #  print "i:",i 
   j=i
   j+=i
   #j+=i
   while j<n:
    A[j]=1
    j+=i
   # print "j:",j
  i+=1
 return A


#print eras_sieve_v1(10)
B=eras_sieve_v1(12)

print B

for i in xrange(2,len(B)):
  if B[i] == 0: print i
