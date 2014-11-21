#!/usr/bin/python
import getopt
import sys
import time
import os
import subprocess 
import json

#corehash={'coredump1':'/home/lherrada/programming/C/coredump/coredump1',
#          'in.tftpd': '/usr/sbin/in.tftpd'}

corehash={}
JSONPATH="/etc/coredumps/core.json"

#Getting binaries path from json configuration files
try:
 f=open(JSONPATH)
 corehash=json.load(f)
except Exception as e:
 print e
 sys.exit(1)

#print corehash
f.close()

#Forcing script to accept only -e and -t parameters 
try:
 opts,args = getopt.getopt(sys.argv[1:],'e:t:')
except getopt.GetoptError as e:
 print "Wrong arguments provided"
 sys.exit(1)

basepath="/var/coredumps"
if os.access(basepath,os.F_OK):
 if os.access(basepath,os.W_OK):
  pass
 else:
  basepath='/tmp'
else:
  basepath='/tmp'

opts=dict(opts)
dirname=opts['-e']+'-'+time.strftime('%Y-%m-%d_%H-%M', time.localtime(int(opts['-t'])))
os.chdir(basepath)
if not os.access(dirname,os.F_OK): os.mkdir(dirname)
corename=opts['-e']+'.core'
corename=os.path.join(basepath,dirname,corename)

f=open(corename,'w')

#Writing coredump on file
for line in sys.stdin:
 f.write(line) 

CORESH="/bin/core.sh"

f.close()
#command= "/home/lherrada/programming/C/coredump/core.sh %s %s" % (corehash[opts['-e']],corename)
command= "%s %s %s" % (CORESH,corehash[opts['-e']],corename)
#print command
subprocess.Popen(command,stdout=subprocess.PIPE,shell=True) 
