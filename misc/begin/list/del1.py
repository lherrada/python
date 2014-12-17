#!/usr/bin/python

def main():
 vowels=['a','e','i','o','u']
 
 for i in vowels:
  print i

 del vowels[0]
 print vowels 
 
 hash={'Rossy':'Peru','Ivonne':'Colombia','Sonia':'Canada'}
 hash['Consuelo']='Mexico'

 del hash['Sonia']
 print hash

 print "Rossy is from %(Rossy)s and Ivonne is from %(Ivonne)s" % hash

if __name__ == '__main__':
 main()
 
