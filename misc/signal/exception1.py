#!/usr/bin/python

try:
 raise Exception("There was an error","Fatal type")
except Exception as inst:
 #print dir(inst)
 #print type(inst)
 print inst.args
 print inst.__str__()
 print inst
 x,y=inst.args
 print "x= ",x
 print "y= ",y

