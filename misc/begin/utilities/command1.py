#!/usr/bin/python
import commands
import os
import sys

#cmd='pwd'
#cmd=r'ls -l'
cmd='ls -l'
print "Command to run: ",cmd

(status,output)=commands.getstatusoutput(cmd) 
#print "Status: %d --- output: %s" % (status,output)

cmd='cat test3.txt'
cmd='sleep 1000'
status,output=commands.getstatusoutput(cmd)

print "STATUS: ",status 

if status: 
 sys.stderr.write(output + '\n')
 sys.exit(2)

print output

