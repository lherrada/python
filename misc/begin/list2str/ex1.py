#!/usr/bin/python
import string
import array
import time

def timing(f,n,m):
 #print f.__name__
 r=range(0,n)
 t1=time.clock()
 for i in r:
  f(m)
 t2=time.clock()
 print "Time elapsed for %s: %7.6f" % (f.__name__,round(t2-t1,3))


def f1(list):
 mystr = ""
 for item in list:
  mystr = mystr + ' ' + chr(item)
 return mystr

def f2(list):
 return reduce(lambda x,y: x + ' ' + chr(y),list,'')

def f3(list):
 string = " "
 for char in map(chr,list):
  string=string + ' ' + char
 return string

def f4(list):
 string = ""
 lchr=chr
 for item in list:
  string=string + ' ' + lchr(item)
 return string

def f5(list):
  string = ""
  for i in range(0, 256, 16): # 0, 16, 32, 48, 64, ...
   s = ""
   lchr=chr
   for character in map(lchr, list[i:i+16]):
   # s = s + character
    string = string + character 
  return string

def f6(list):
 return string.joinfields(map(chr,list)," ")

def f7(list):
 mystring=''
 for i in range(0,256,16):
  mystring=mystring+string.joinfields(map(chr,list[i:i+16]),"")  
 return mystring

def f8(list):
 return array.array('B',list).tostring()
 

if __name__ == '__main__':
 import timeit
 #a=[97,98,99,100]
 a='range(1,256)'
 sa=str(a)
 #print f1(range(97,101))

 mynumber=100000
 #mynumber=1

 s="f1(" + sa + ")"
 time1=timeit.timeit(s,setup="from __main__ import f1",number=mynumber)
 print "%s: %7.6f secs" % (s,time1)

 s="f2(" + sa + ")"
 time1=timeit.timeit(s,setup="from __main__ import f2",number=mynumber)
 print "%s: %7.6f secs" % (s,time1)

 s="f3(" + sa + ")"
 time1=timeit.timeit(s,setup="from __main__ import f3",number=mynumber)
 print "%s: %7.6f secs" % (s,time1)

 s="f4(" + sa + ")"
 time1=timeit.timeit(s,setup="from __main__ import f4",number=mynumber)
 print "%s: %7.6f secs" % (s,time1)

 s="f5(" + sa + ")"
 time1=timeit.timeit(s,setup="from __main__ import f5",number=mynumber)
 print "%s: %7.6f secs" % (s,time1)

 s="f6(" + sa + ")"
 time1=timeit.timeit(s,setup="from __main__ import f6",number=mynumber)
 print "%s: %7.6f secs" % (s,time1)

 s="f7(" + sa + ")"
 time1=timeit.timeit(s,setup="from __main__ import f7",number=mynumber)
 print "%s: %7.6f secs" % (s,time1)
 
 s="f8(" + sa + ")"
 time1=timeit.timeit(s,setup="from __main__ import f8",number=mynumber)
 print "%s: %7.6f secs" % (s,time1)

 print "="*30

 for myf in [f1,f2,f3,f4,f5,f6,f7,f8]:
  timing(myf,mynumber,range(1,256))

#print f7(range(1,256))

#print "F1:"

#print f1(a)
#print "F2:"
#print f2(a)

#print "F1:"
#print f1(a)
#print "F2:"
#print f2(a)
