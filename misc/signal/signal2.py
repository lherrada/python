#!/usr/bin/python
import signal,os
import time
import subprocess
import random

def handler(signum,frame):
 print "Signal handler called: %d" % signum
 print "Timeout."
 exit(3)
 #raise IOError("CANNOT open device")

signal.signal(signal.SIGALRM, handler)

for i in range(5):
 pid=os.fork() 
 if pid == 0:
  command="curl http://precise:8080/index.html 2>/dev/null"
  random.seed()
  timeout=random.randint(1,5)
  print "Child pid is %d - timeout: %d " % (os.getpid(),timeout)

  signal.alarm(3)
  #time.sleep(timeout) 
  p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
  signal.alarm(0)
  result=p.communicate()[0]
  print result,
  exit(0)

results={} 

while True:
 try:
  (pid,status)=os.waitpid(-1,os.WNOHANG) 
  results[pid]=status>>8 
 except OSError:
  break  

print results



"""
signal.alarm(4)
#fd = os.open('/dev/ttyS0', os.O_RDWR)
time.sleep(5)
signal.alarm(0)

signal.alarm(4)
time.sleep(3)
signal.alarm(0)

print "="*20
"""
