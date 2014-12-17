import math

def eras_sieve_v1(n):
 A=[0 for i in range(0,n)]
 i=2
 while i<n:
  if A[i]==0: 
   #print "i:",i 
   j=i
   while j<n:
    A[j]=1
    j+=i
  #  print "j:",j
  i+=1
  
def eras_sieve_v2(n):
 A=[1 for i in range(0,n)]
 i=2
 while i<math.sqrt(n):
  if A[i] == 1:
   j=i**2
   while j<n:
    A[j]=0
    j+=i
  i+=1  
 
 for i in xrange(2,len(A)): 
  if A[i] == 1: print i



 
eras_sieve_v2(20)
