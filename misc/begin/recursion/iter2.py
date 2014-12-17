#!/usr/bin/python

myfile='file1.txt'

with open(myfile) as fp:
 for line in iter(fp.readline,'L\n'):
  print line,

fp.close()

print '=' * 30

fp=open(myfile)
it=fp.__iter__()

#for i in it:
# print i,

#print next(it),
#print next(it),
#print it.next(),

print next(it,'End'),
print next(it,'End'),
print next(it,'End'),
print next(it,'End\n'),

print '=' * 30

mylist=['a','b','c','d']

it=mylist.__iter__()

while True: 
 a=next(it,'END')
 if a == 'END': break
 else:
  print "->",a 

print '=' * 30
it=mylist.__iter__()

#print dir(it)

