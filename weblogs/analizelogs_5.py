#!/usr/bin/python
#The numbers of successful and failed responses per website URL 

import re

def dumper(myhash):
 for k,v in myhash.iteritems():
  print "{0}: {1}".format(k,v)


logs=open('NASA_access_log_Jul95')
#logs=open('nasa.log')

myhash={}
j=0

for line in logs:
 j+=1
 line=line.strip('\n')
# mylist=re.split('\s+',line)
 lookup=re.search(r'"(.*?)"\s+(\d+)',line)

 try:
  website=lookup.group(1)
  website=re.search(r'(GET)?\s+(.*?)\s+(HTTP)?',website)
  website=website.group(2)  
  errorcode=lookup.group(2)
 except AttributeError: 
  pass
 
 #print "%s : %s" % (website,errorcode) 
 mytuple=(website,errorcode)

 if mytuple in myhash:
  myhash[mytuple]+=1
 else:
  myhash[mytuple]=0
  myhash[mytuple]+=1


#dumper(myhash)
scodes=['200','304','302']
#scodes=['404']

for key in sorted(myhash,key=myhash.__getitem__,reverse=True):
 if key[1] not in scodes:
  pass
 else: 
  print "{0}: {1}".format(key,myhash[key]) 
