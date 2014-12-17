#!/usr/bin/python

import shelve
db=shelve.open('persondb')

for i in db.keys():
 print db[i]
