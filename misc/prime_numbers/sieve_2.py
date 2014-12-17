def eras_sieve(n):
 sieve=[0 for i in range(0,n)]
 i=2
 while i<n:
  if sieve[i] == 0:
  # print i 
   j = i
   j+=i
   while j<n:
    sieve[j] = 1
    j+=i
  i+=1
 return sieve   


B=eras_sieve(20);
#print B

for k in xrange(2,len(B)):
 if B[k] == 0:
  print k
  
