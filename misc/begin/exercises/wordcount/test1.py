#!/usr/bin/python

def main():



 dict1={}
 

 listA=['comer','salir','pues','comer','pues','pues','dormir']

 count=2 
 dict1[listA[0]]=count+1
 
 for i in listA:
  dict1[i]=0

 dict1['dormir']+=1
 
 #print type(dict1['comer'])

 for i in listA:
  dict1[i]+=1
 
 print dict1

 dict1={'Brazil':5,'Argentina':2,'Alemania':4}

 print "="*30

 for key in sorted(dict1.iterkeys()):
  print key
 
 print "="*30

 print " ==> %s" % dict1.items()
 a=dict1.items()

 print a[1]
 
 print dict1.items()
 print "="*50 

 for k,v in dict1.items():
  print k + ':' + str(v)
 
# def myfn(string):
#  return :wq



if __name__ == '__main__':
 main()
