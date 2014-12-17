#!/usr/bin/python

def main():
 tuple=(5,4,6)
 tuple=(1,2,3)
  
 for i in tuple:
  print i

 print "size: " + str(len(tuple))
 print tuple[2]
 print tuple

 tuple2=(3)
 print tuple2

 (x,y,z)=tuple1()
 print (x,y,z)
 print x

def tuple1():
 return (21,34,12)

if __name__ == '__main__':
 main()
