#!/usr/bin/python
X=50
y=100

def selector():
 import __main__
 print __main__.X
 X=30
 print X

selector()
