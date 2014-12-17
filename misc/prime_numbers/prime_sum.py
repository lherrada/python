import math

def get_primes(number):
 while True:
  if is_prime(number):
   yield number
  number +=1

def is_prime(number):
 if number > 1:
  if number == 2: return True
  if number % 2 == 0: return False

  for current in range(3,int(math.sqrt(number)+1),2):
   if number % current == 0:
    return False
  return True
 return False


def solve_number_10():
 total=2
 limit=2000000
 for next_prime in get_primes(3):
  if next_prime < limit:
   total += next_prime 
  else:
   print total
   return

def smallest_prime_greater_than_n(number):
 return next(get_primes(number))
 
for i in range(1,4):   
 print smallest_prime_greater_than_n(10**i)


#solve_number_10()
