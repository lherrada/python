#!/usr/bin/python

def main():
 a=1
 if a==0:
  def f1(): print "I am f1"
 else:
  def f1(): print "I am second version"
 f1()


if __name__=='__main__': 
 main()
 
 
