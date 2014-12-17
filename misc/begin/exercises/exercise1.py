#!/usr/bin/python

#Write an script that allows you to put as an option a file , then reads the file and put in
# dict the data in that file 

import sys,getopt

#print sys.argv[1:]

try:
 opts,args = getopt.getopt(sys.argv[1:],'i:o:v',['input=','output=','verbose'])
except getopt.GetoptError: 
 print "Usage: "
 print "%s -i <inputfile> -o <outputfile>" % sys.argv[0] 
 sys.exit(1);


for opt,arg in opts:
 if opt == '-h':
  print "%s -i <inputfile> -o <outputfile>" % sys.argv[0] 
  sys.exit()
 elif opt in ("-i","--input"):
  inputfile = arg
 elif opt in ("-o","--output"):
  outputfile = arg
    
print "input file: %s" % inputfile
print "output file: %s" % outputfile


#myfile=open(

#print opts
#print "="*30
#print args


