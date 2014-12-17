#!/usr/bin/python
import os,sys
import getopt

def testdir(dir):
 if os.path.isdir(dir) and not os.path.islink(dir):
  return True
 else:
  return False


def mylistdir(dirname):
 mylist=[os.path.join(dirname,i) for i in os.listdir(dirname)]
 mylist2=[ os.path.abspath(i) for i in mylist]
 #return filter(os.path.isdir and not os.path.islink,mylist2)
 return filter(testdir,mylist2)

 #return filter(os.path.isdir,mylist2) 

def mylistdir2(dirname):
 mylist=[os.path.join(dirname,i) for i in os.listdir(dirname)]
 mylist2=[ os.path.abspath(i) for i in mylist]
 #return [ i for i in mylist if os.path.isdir(i) or os.path.islink(i) ]
 return [ i for i in mylist if os.path.isdir(i) and not os.path.islink(i) ]

try:
 opts,args= getopt.getopt(sys.argv[1:],'d:')
except getopt.GetoptError as err:
 print err
 sys.exit[1];

dict1=dict(opts)

print mylistdir(dict1['-d'])

for link in  mylistdir(dict1['-d']):
 linkname=link + '_symlink'
# print namelink
 if not os.path.exists(linkname):
  os.symlink(link,linkname)
 else:
  print "Symbolic link %s already exists." % linkname 
