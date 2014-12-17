#!/usr/bin/python
import signal
import re

def alarm_received(n,stack):
 return

signal.signal(signal.SIGALRM,alarm_received)

hash_signal={}
for mysignal in dir(signal):
 if re.match("^SIG",mysignal):
  ns=getattr(signal,mysignal)
  hash_signal[mysignal]=ns 

#print hash_signal

#for (k,v) in hash_signal.iteritems():
# print "%s: %d" % (k,v)


for mysignal,ns in sorted(hash_signal.iteritems(),key=lambda (k,v):(v,k)): 
 if ns != 0:
  #print "ns -> %d" % ns
  #print "%s: %d" % (mysignal,signal.getsignal(ns))
  print "%s(%d): " % (mysignal,getattr(signal,mysignal)),signal.getsignal(ns) 










