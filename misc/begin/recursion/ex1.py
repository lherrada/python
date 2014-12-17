#!/usr/bin/python

def factorial(n):
 print "Factorial called with n=%d" % n
 if n == 1:
  return 1
 else:
  return n * factorial(n-1)


#if num == '0': print "Enter the end"
#else: print "Enter to continue"

while True:
 num=raw_input("Input number (0 to end): ")
 if num == '0':
  break
 else:
  print factorial(int(num)) 

#while  == '0':
# print factorial(int(num))
 
