from __future__ import generators

def eratosthenes(maxnum):
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while q <= maxnum:
        #print "->",q	
        #print D
        if q not in D:
            yield q       # not marked composite, must be prime
            D[q*q] = [q]  # first multiple of q not already marked
        else:
            for p in D[q]:  # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]        # no longer need D[q], free memory
        q += 1
        print D

#for p in eratosthenes(15): print p,
for p in eratosthenes(15): print 
