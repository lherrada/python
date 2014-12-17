#!/usr/bin/python
import os
import subprocess 

print os.getpid()

#subprocess.call(['sleep','500'])

#sp=subprocess.Popen(['sleep','400'])
sp=subprocess.Popen(['ps','aux'])
print('PID is ' + str(sp.pid))
