#!/usr/bin/python

try:
 import redis 
 print "Redis installed"
except ImportError:
 print "No Redis Module"

r=redis.StrictRedis(host='192.168.0.102',port=6379,db=0)

r.set('name','Luis')
print r.get('name')
print r.get('name')
print r.get('name')
