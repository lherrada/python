#!/usr/bin/python

while True:
 try:
  x=int (raw_input("Please enter your age: "))
  #print "Your age is %d" % (x) 
  #break
 except ValueError:
  print "No valid value. Try again ..."
