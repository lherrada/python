#!/usr/bin/python
import subprocess
import os
import httplib

URL=['cpan.org','google.com','tools.pingdom.com']

children=[]
for url in URL:
 try:
  newpid=os.fork()
 except OSError:
  print "Cannot fork"
  exit(1)

 if newpid != 0:
  children.append(newpid)
 else:
  #print subprocess.Popen(["curl",url],stdout=subprocess.PIPE).communicate()[0]
  #subprocess.call(["curl",url])
 
  http=httplib.HTTPConnection(url)
  http.request('GET','/')
  res=http.getresponse()
  data=res.read()
  print url
  print data
  exit(0)

kid=0;
#while kid>=0:
while True:
 try:
  #(kid,status)=os.waitpid(-1,os.WNOHANG)
  os.waitpid(-1,os.WNOHANG)
  #print "%d: %d" %(kid,status)  
 except OSError:
  break

 
#for pid in children:
# os.waitpid(pid,0)

