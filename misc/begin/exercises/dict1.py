#!/usr/bin/python

def main():
 dict={'Luis': (37,'US','single'),'Silvia': (36,'Peru','married')} 
 
 for key in dict.keys():
  print key

 for (age,country,status) in dict.values():
  print "My age is %d. I live in %s and my status is %s" % (age,country,status)  

 #(age,country,status)=(20,'Mexico','single')
 #print country

 for key in dict.keys():
  print "Your name is %s and your age is %d. Your status is %s" % (key,dict[key][0],dict[key][2]) 

if __name__ == '__main__':
 main()
