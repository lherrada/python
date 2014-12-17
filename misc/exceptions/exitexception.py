import sys

def f1():
 sys.exit(1) 
 #exit(1) 
 #return 1

if __name__ == '__main__':
 try:
  f1()
 except:
  #print "[%s]: %s" % (e.__class__.__name__,e) 
  print "Exception caught"

 print "-" * 30

