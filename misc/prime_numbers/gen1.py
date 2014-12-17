import time
import math

def gen1(number):
 while True:
  yield number
  number*=2


def gen2(number):
 while (number < 100):
  if number % 6 == 0:
   yield number
  number+=1






def eratosthenes(maxnum):
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while q <= maxnum:
        if q not in D:
            yield q       # not marked composite, must be prime
            D[q*q] = [q]  # first multiple of q not already marked
        else:
            for p in D[q]:  # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]        # no longer need D[q], free memory
        q += 1


def isprime(number):
 if number > 1:
  if number == 2: return True  
  if number % 2 == 0: return False
  
  for current in range(3,int(math.sqrt(number)+1),2):
   if number % current == 0:
    return False
  return True
 return False
 

def getprime(limit):
 i=2
 while i<limit:
  if isprime(i): yield i 
  i+=1

value=2000000
'''
sum=0
for i in eratosthenes(value):
 sum+=i 
print sum
'''

sum=0
for i in getprime(value):
 sum+=i 
print sum


'''
for i in gen1(1):
 print i 
 time.sleep(1)	
'''
'''
for i in gen2(1):
 print i
 time.sleep(1)
'''
