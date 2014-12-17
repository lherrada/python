import sys

while True:
 try:
  a=float(raw_input('Enter number a: ' ))
  b=float(raw_input('Enter number b: ' ))
  n=a/b
 except Exception as e:
  print "[%s] : %s" % (e.__class__.__name__,e)  
  #sys.exit(1)
 else:
  print "--> %.3f" % (n) 
  #break
