#!/usr/bin/python

import signal
import os
import time
import inspect

def receive_signal(signum,stack):
 print 'Received: ',signum
 #print 'Stack: ',stack
 #print dir(stack)
 print inspect.getframeinfo(stack)

signal.signal(signal.SIGUSR1,receive_signal)
signal.signal(signal.SIGUSR2,receive_signal)

print "My PID is : ",os.getpid()

while True:
 print 'Waiting ...'
 time.sleep(3)
