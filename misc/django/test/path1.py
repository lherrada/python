#!/usr/bin/python
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#path1='/home/lherrada/programming/python/django/test'
path1='nobody'
#path2='/home/lherrada/programming/python/django/test/file1.txt'
path2='file1.txt'

print os.path.abspath(path1)
print os.path.abspath(path2)

path3='/home/lherrada/programming/python/django/test/file1.txt'
print os.path.basename(path3)

path4='/home/lherrada/programming/python/django/test1/'
print os.path.basename(path4)

print "Dirname:"
print os.path.dirname(path3)

print "Dirname of a file"
print " -->",os.path.dirname(path2)

#print BASE_DIR
print os.path.dirname(__file__) 
print __file__
