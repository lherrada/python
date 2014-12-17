#!/usr/bin/python

import subprocess
import os,sys
command=['stat','test2.txt']

#result=subprocess.call(command)

command=['find','/home/lherrada/programming/python/begin/']
p=subprocess.Popen(command,stdout=subprocess.PIPE)

output=p.stdout.read()
print "=" * 20

#output,err=p.communicate()
output=output.strip('\n')
mylist=output.split('\n')

for i in mylist:
 if os.path.islink(i) and not os.path.exists(i):
  print "Broken Link: %s" % i
#subprocess.check_output(["echo", "Hello World!"])

#print "--->",result

command=['cat']

f=open('test2.txt')

p=subprocess.Popen(command,stdout=subprocess.PIPE,stdin=f)
p.wait()
output=p.stdout.read()
print output,
f.close()


f=open('test2.txt')
command=['grep','-R','entrevista'] 

message="La entrevista sera facil"


#p=subprocess.Popen(command,stdout=subprocess.PIPE,stdin=f)
p=subprocess.Popen(command,stdout=subprocess.PIPE,stdin=f)
output=p.stdout.read()
print output,

print "=" * 30

command=['tr','a-z','A-Z']

p=subprocess.Popen(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
p.stdin.write('luis alberto')
output,error=p.communicate()
print output,
p.stdin.close()




