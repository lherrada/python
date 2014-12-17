#!/usr/bin/python
import signal
import os

def do_exit(sig,stack):
 raise SystemExit('Quiting...') 

signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.signal(signal.SIGUSR1,do_exit)

print 'My PID: ',os.getpid()

signal.pause()


