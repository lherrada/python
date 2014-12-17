#!/usr/bin/python

from collections import defaultdict
import datetime


def linkfirst(i):
 return i

alt= [ linkfirst(i)
      for i in range(1,5) ] 

list1=['a',
       'b',
       'c'
      ]

print "TYPE: %s" % type(alt)

mx=max(alt)
print mx


h1=defaultdict(int)
print repr(h1)

x=datetime.date.today()
print "Today's date is %s ..." % x 
print "Today's date is %r ..." % x 



#print dir(alt)

#print "MAX: %d" % mx
#print type(alt)


