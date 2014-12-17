#!/usr/bin/python

def main():
 #myfile=open('countries.txt','r') 
 myfile=open('alice.txt','r') 

 #string=myfile.readline()

 #while string:
 # print string.upper(),
 # string=myfile.readline()
 count=0

 for line in myfile:
  count=0
  for i in line:
   if i == 'e':
    count=count+1 
  print "e: " + str(count)

 f=open('first.txt','w')

 friends=('Ivan','Tello','Ayala')

 for i in friends:
  f.write(i+'\n')

 f.close()

if __name__ == '__main__':
 main()
