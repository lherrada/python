#!/usr/bin/python

def gen_primes():
 D={}
 q=2
 while True:
  if q not in D:
   yield q
   D[q*q] = [q]
  else:
   for p in D[q]:
    D.setdefault(p+q,[]).append(p)
   del D[q]
  q+=1
 
def PrimeMover(n):
 j=0
 for i in gen_primes():
   j+=1 
   if (j == n): return i

input1=int(raw_input("Type numth: "))

print PrimeMover(input1)
