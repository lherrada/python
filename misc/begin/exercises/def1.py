#!/usr/bin/python

def general(func,arg):
 apply(func,(arg,))

def name(x):
 print "Your name is " + x

def age(n):
 print "Your age is %d" % n

print "=" * 30

datain=[(name,"Erikita"),(age,38)]

for i,j in datain:
 apply(i,(j,)) 

for i,j in datain:
 i(j)

#general(name,"Erikita")
#general(age,38)

#name("Erika")
#x=name
#x("Luis")
#age(37)


