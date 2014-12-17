from streams import Processor
import sys

def converter(string):
 return string.upper()

class Uppercase(Processor):
 def converter(self,string):
  return string.upper() 

class HTMLize:
 def write(self,data):
  print "<h1> %s </h1>" % data.rstrip()



if __name__ == '__main__':
 #s1=Uppercase(open('reader1.txt'),sys.stdout)
 #s1.process()


 s2=Uppercase(open('reader1.txt'),sys.stdout,converter)
 s2.process()

 print "="*30

 s3=Uppercase(open('reader1.txt'),HTMLize())
 s3.process()
