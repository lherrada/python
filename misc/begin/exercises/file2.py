#!/usr/bin/python

def main():
 f=open('first.txt','r')
 
# a=f.readline()
# print a,

 while True:
  a=f.readline()
  print a,
  if not a: break


# while f.readline():
#  print f.readline()

if __name__ == '__main__':
 main()
