#!/usr/bin/python

foo=1
def test():
 global foo
 foo+=1
 print "Local: %d" % foo 

def test2():
 global foo
 print foo
 foo=4

test() 
test() 
#print "Global: %d" % foo

test2()
