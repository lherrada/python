#!/usr/bin/python
import random

def rgen(n):
 for i in xrange(n):
  num=random.randint(0,99)
  yield num


nrandom=rgen(20) 

for i in nrandom:
 print i
