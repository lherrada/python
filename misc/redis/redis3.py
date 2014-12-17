#!/usr/bin/python
##!/usr/bin/python2.7

import redis

rserver = redis.Redis('localhost')

a=rserver.set('name','Luis')

#print dir(rserver)
print type(rserver)
print a
print "Getting value: ",rserver.get('name')
