#!/usr/bin/python

with open('brothers.txt') as f:
 for line in f: 
  print line,

print "=" * 20
f=open('brothers.txt')
#print f.read(),
a=f.read()
print type(a)

print "=" * 40
f=open('brothers.txt')
while True:
 line=f.readline()
 if not line: break
 else: print line,

print "=" * 40
f=open('brothers.txt')

while f.readline():
 print f.tell()
##########################################

print "=" * 40
f=open('brothers.txt')


f.seek(113,0)
nlines=3
counter=1

#for line in xrange(2):
while counter<nlines:
 f.seek(-2,1) 
 if f.read(1) == '\n':
   counter+=1

 
#while char != '\n':
# f.seek(-2,1) 
 #char=f.read(1)
 #array.append(char) 
 #print f.tell()
 
print f.tell()
print f.read(),
