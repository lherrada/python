#!/usr/bin/python

from pets import Pet

mydog=Pet("Bobby","dog")

print "My petname is",mydog.getName()
print "My pet is a",mydog.getSpecies()
print "Info summary:",mydog.__str__()

print "Second way to obtain name:",Pet.getName(mydog)

print mydog

mydog.age=5

if hasattr(mydog,'age'):
 print "Dog age is",mydog.age

print "=" * 20

mycat=Pet("Michy","cat")
print mycat

myhorse=Pet("Mr.T","horse")
print myhorse
