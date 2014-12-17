#!/usr/bin/python
import sys
import inspect

#raise IOError,"Cannot open file"
try:
 myfile=open("data1.txt")
except:
 print "Unexpected Error: "
 for i in sys.exc_info():
  print i 

'''
sys.exc_info()
This function returns a tuple of three values that give information about the exception that is currently being handled. The information returned is specific both to the current thread and to the current stack frame.
The values returned are (type, value, traceback). Their meaning is: type gets the exception type of the exception being handled (a class object); value gets the exception parameter (its associated value or the second argument to raise, which is always a class instance if the exception type is a class object); traceback gets a traceback object (see the Reference Manual) which encapsulates the call stack at the point where the exception originally occurred.

'''



 print "="*30
 a=sys.exc_info()[2]
 print a.__class__
 print type(a)
 print "="*30

 if isinstance(a,list): print "Yeahhh!"
 
 
#  print i.__class__ 
#  if type(i) is 'traceback': print inspect.getframeinfo(sys.exc_info()[2])


