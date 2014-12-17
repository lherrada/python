#!/usr/bin/python
# -*- coding: latin-1 -*-

def myf(mystring):
 return len(mystring) 



dict1={ "merry":"god",
        "christmas":"jul",
        "and":"och",
        "happy":"gott",
        "new":"nytt",
        "year":"p" }

#dict2 = {k : v for k, v in dict1.iteritems()}

dict2=dict((k,myf(v)) for k,v in dict1.iteritems())

print dict2

#for i in dict1.items():
# print i
