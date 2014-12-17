#!/usr/bin/python
import sys
import traceback
import inspect

def myconverter(data):
 return data.upper()

def processor(reader,converter=myconverter,writer=None):
 while True:
  data=reader.readline()
  data=converter(data)  
  writer.write(data)
  print data,  
  if not data: break

try:
 f=open("reader1.txt")
 w=open("writer1.txt","w")
except:
 for i in sys.exc_info():
  print type(i),i

processor(f,myconverter,w)


 #if i.__class__.__name__ == 'traceback': print "Traceback detected"
 #print "Unexpected I/O error"
 #traceback.print_exc()
 #traceback.print_exception(None,None,traceobj)

#print inspect.getframeinfo(sys.exc_info()[2]) 
#print "="* 30

#traceback.print_tb(sys.exc_info()[2])

