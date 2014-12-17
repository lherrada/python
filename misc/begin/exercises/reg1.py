#!/usr/bin/python
import re

def main():

 #Dict
 dict1={'Melissa':27,'Silvia':30,'Luis':37,'Silvia':36}

 if 'Melissa' in dict1:
  print "She is %(Melissa)d old" % dict1 
 
 print "=" * 30

 p=re.compile(r'\s+(\w+)\s+(\w+)\s+(\w+)')

 m=p.match("  Melissa	Leslie			Silvia")
 if m:
  print m.group(1) 
  print m.group(2)
  print m.group(3)
  #print m.group()

 print "=" * 30

 string='Lucia donde estas, te sigo buscando, no se por donde seguir,dime hasta cuando. Luis '

 mymatch=re.search(r'(\bL\w+\b)',string)

 if mymatch:
  print mymatch.group(1) 
  print mymatch.span() 

 print "=" * 50
 
 p=re.compile(r'(\bL\w+\b)')
 mymatch=p.findall(string) 
 print mymatch 
  
 print "=" * 50
 str1 = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher' 
 p=re.compile(r'([\w\.-]+)@([\w\.-]+)')
 mymatch=p.findall(str1) 
 print mymatch 

 str2='yahoo:35 --- citibank:50 ldk:11 === fslr:60'
 p=re.compile(r'(\w+):(\w+)')
 mymatch=p.findall(str2) 
 print mymatch
  
 iteration=p.finditer(str2)
 for match in iteration:
  print match.span()

if __name__ == '__main__':
 main()
