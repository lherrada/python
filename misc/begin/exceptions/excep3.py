#!/usr/bin/python

import sys
#import yaml

try:
 f=open('file1.txt','r')
 s=f.readline()
 i=int(s.strip())
except IOError as e:
 print "I/O error({0}): {1}".format(e.errno,e.strerror)
except ValueError:
 print "Could not convert data to an integer."
#except:
else:
 print "Unexpected Error:", sys.exc_info()[0]
 
 #raise

print "Outcome reached!!!"
