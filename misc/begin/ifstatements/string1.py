#!/usr/bin/python

def main():
 a=' Luis Herrada M. '
 print a
 print (a.lower()).strip() 
 
 b='2luis';

 if b.isdigit():
  print "b is digit"
 elif b.isspace():
  print "b is a space"
 elif b.isalpha():
  print "b is alphanumeric"
 else: print "b cannot be cathegorized" 
 
 c='Luis:Silvia:Leslie:Melissa'
 lista=c.split(':')
 print lista

 d='Lets remove all e vowels from the text'
 print d.replace('e',' ')

if __name__ == '__main__':
 main()
