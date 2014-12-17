#!/usr/bin/python

def factorial(n):
 print "Factorial called with n=%d" % n
 if n == 1:
  return 1
 else:
  res = n * factorial(n-1)
  print "Middle result for: ",n," *factorial(",n-1,"): ",res
  return res


#if num == '0': print "Enter the end"
#else: print "Enter to continue"

while True:
 num=raw_input("Input number (0 to end): ")
 if num == '0':
  break
 else:
  fact=factorial(int(num));
  print "Result: ",fact

#while  == '0':
# print factorial(int(num))
 
