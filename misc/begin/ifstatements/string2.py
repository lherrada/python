#!/usr/bin/python

def main():
 country="Germany"

 print country[1:]
 print "=========" 
 print country[:2]
 print country[2:]

 print country[:]
 print country[:-4]
 print country[-4:]

 ustring = u'A unicode \u020e string \xf1 \xc2'
 print ustring.encode('utf-8')

 unistring= u'Unicode \xd8 \xeb' 
 
 utf_string=unistring.encode('utf-8')
 
 t=unicode(utf_string,'utf-8')
	
 if (t == unistring):
  print "Success!!!!"	


 #for i in range(len(country)):
 # print country[i]

if __name__ == '__main__':
 main()

