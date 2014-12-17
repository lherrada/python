#!/usr/bin/python

import shelve
from person import * 


db=shelve.open('persondb')

lhm=Person('Luis','Herrada',None,None,37)
rga=Manager('Ruben','Gutierrez','Impsat',37)


for instance in (lhm,rga):
 db[instance.name + " " + instance.lastname]=instance

db.close()

db=shelve.open('persondb')

print "DB len is %d" % len(db)

for i in db.keys():
 #print db[i].__dict__ 
 print db[i] 







