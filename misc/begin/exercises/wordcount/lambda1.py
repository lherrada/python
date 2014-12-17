#!/usr/bin/python

def main():
 print f1(2,5,5) 

 g=lambda a=1,b=2,c=3: a**2+b**2+c**2
 print g(0)
 
 h=lambda a,b: [a**2,b**2]
 
 for i in h(1,2):
  print i
 
 print "="*40

 squares = []

 for i in h(2,3): 
  squares.append(i**3) 

 print squares

 for i in f2(1,4,5):
  squares.append(i) 

 print squares

def f1(x=1,y=2,z=3): 
 return x+y+z

def f2(x,y,z):
 return (x,2*y,3*z)

if __name__ == '__main__':
 main()

