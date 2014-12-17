#!/usr/bin/python

def main(): 
 a=[3,1,6,2]
 print sorted(a)
 print a

 list=['a2','b5','c1']

 print sorted(list,key=mytest)

def mytest(list):
 return list[-1]

if __name__ == '__main__':
 main() 
