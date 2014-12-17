#!/usr/bin/env python
import time
from subprocess import Popen, PIPE

LINE_BUFFERED = 1

#NOTE: the first argument is a list
#p = Popen(['tr','a-z','A-Z'], bufsize=LINE_BUFFERED, stdin=PIPE,stdout=PIPE)
#p = Popen(['tr','a-z','A-Z'],stdin=PIPE,stdout=PIPE)
p = Popen(['tr','a-z','A-Z'],stdin=PIPE)
for cmd in ["Luis ALberto Herrada"]:
#    time.sleep(1) # a delay to see that the commands appear one by one
    p.stdin.write(cmd)
    #out,error=p.communicate()
    #print out
    # even without .flush() it works as expected on my machine
p.stdin.close()
