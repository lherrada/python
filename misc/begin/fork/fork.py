#!/usr/bin/python
#import subprocess
import httplib 
import os
import time
import subprocess
import sys

URL=['google.com','python.org','cpan.org']
#f=open(os.devnull,'w')
#sys.stdout=f 
#URL=['http://'+url for url in URL]

children=[]
for url in URL:
 newpid=os.fork()
 if newpid != 0:
  children.append(newpid) 
 else:
  print "="*20
  print url
  subprocess.call(["curl",url])
  #print os.popen("curl " + url).read()
  #print subprocess.Popen(['curl',url],stdout=subprocess.PIPE).stdout
  #print subprocess.Popen(['curl',url],stdout=subprocess.PIPE).communicate()[0]
  #httpconnection=httplib.HTTPConnection(url) 
  #httpconnection.request('GET','/')
  #res=httpconnection.getresponse()
  #data=res.read()
  #print data
  #print url
  #time.sleep(5)
  exit(0)
"""
kid=0;
while kid>=0:
 try:
  (kid,status)=os.waitpid(-1,os.WNOHANG)
 except OSError:
  pass
"""

for pid in children:
 os.waitpid(pid,0)


"""
"""
 #output=subprocess.Popen(['curl',url],stdout=subprocess.PIPE).communicate()[0]
 #p=subprocess.Popen(['echo',url],stdout=subprocess.PIPE)
 #output,error=p.communicate()
 #print output
