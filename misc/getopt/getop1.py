#!/usr/bin/python

import getopt
import sys
import re
import subprocess

def help():
 print "Usage: "
 print "%s -h <hostfile>" % sys.argv[0]

if not sys.argv[1:]:
 help()
 exit()

try:
 options=getopt.getopt(sys.argv[1:],'h:t',['hostname=',',timeout'])
except getopt.GetoptError:
 help()
 exit()

options=dict(options[0])

try:
 filename=open(options['-h'])
except IOError as e:
 print "Error opening file %s" % e.strerror

myhash={}

for line in filename:
 line=line.strip()
 p=subprocess.Popen(['echo','-n','http://' + line + '/status.html'],stdout=subprocess.PIPE) 
 (result,errorcode)=p.communicate()
 myhash[line]=result 

#print myhash 

for key in myhash:
 if re.match('OK',myhash[key]):
  print "%s: in rotation" % key
 else:
  print "%s: not in rotation" % key

""" 
myfile=open(options['-h'])

for line in myfile:
 line.strip()
 print line
"""
