#!/usr/bin/python

import module1
print module1.name
print module1._zip

print "="*30
from module1 import *
print name
print _zip


