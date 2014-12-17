#!/usr/bin/python

def main():
 names=['Luis','Ximena','Xavier','Andrea','Patty','Xofo','xina']

 for i in names:
  if i == 'Luis':
   print i
  else: print "===> " + i

 print "=" * 30

 for i in names:
  if i[0] == 'x' or i[0] == 'X':
   print i
 # else: print " ---> " + i

  #print i[0:2].upper()  

# if string[1] == 'i':
#  print "succeess!!!" 
# else: print "Failure!!!"




if __name__ == '__main__':
 main()
