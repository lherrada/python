#!/usr/bin/python

str="Luis Alberto Herrada Mateo"


it=iter(str)

print it.next()
print it.next()
print it.next()
print list(it)

print "=" * 10

mylist=['Luis','Alberto','Herrada','Mateo']
it=iter(mylist)
print it.next()
print it.next()
print list(it)

print "=" * 10

mytuple=('Luis','Alberto','Herrada','Mateo')
it=iter(mytuple)
print it.next()
print it.next()
print list(it)

print "=" * 10

mydict1={'name':'Luis','middlename':'Alberto','lastname1':'Herrada','lastname2':'Mateo'}
it=iter(mydict1)
print it.next()
print it.next()
print list(it)

print "=" * 10
it=mydict1.iteritems()
#for i in it:
# print it.next()

for k,v in mydict1.iteritems():
 print "{0}: {1}".format(k,v)


#print list.__getitem__(0)
