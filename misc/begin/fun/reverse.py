#!/usr/bin/python
import sys,re

file="excerpt1.txt"

try:
 myfile=open(file)
except IOError as e:
 print "Error [{0}]: {1}".format(e.errno,e.strerror)



