#!/usr/bin/python
import re

def main():
 #str1 = raw_input("Your name is: ")
 #print "You said your name is" + str1

 file=open('alice.txt')
 p=re.compile(r'[^a-zA-Z0-9\s+-]')

 dict1={}

 for line in file:
  clean_line=p.sub(' ',line).lower()
  listA=re.split(r'\s+',clean_line) 
  for i in listA:
   if i in dict1:
    dict1[i]+=1  
   else: 
    dict1[i]=0
    dict1[i]+=1	
 
#First method of sorting

 #for i in sorted(dict1,key=dict1.__getitem__,reverse=True):
  #print "%s:%d" % (i,dict1[i])

#Second method of sorting

 for k,v in sorted(dict1.iteritems(),key=lambda (k,v): (v,k),reverse=True):
  print "%s:%d" % (k,v)

# print sorted(dict1.values()) 

  #for k,v in dict1.iteritems():
  # print "%s:%d" % (k,v)

 #for key in sorted(dict1.keys()):
 # print "%s:%d" %(key,dict1[key])

if __name__ == '__main__':
  main()
