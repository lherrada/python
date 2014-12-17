#!/usr/bin/python

def main():
 countries=['Canada','USA','Peru']
 
 for i in countries:
  print i

 print "=" * 10

 for i in range(len(countries)):
  print countries[i]
 
 print countries[-2]

 print "=" * 10
 b=countries; 
 for i in range(len(countries)):
  print b[i]

 print "=" * 10
 #countries+='Mexico'
 countries.append('Mexico')
 for i in countries:
  print i

 print "=" * 20
 countries.extend(['Brazil','Francia']) 
 for i in countries:
  print i

 countries.append('Peru')
 print "=" * 20
 for i in countries:
  print i
  n=countries.index('Peru')

 print " ===> " + str(n)
 
 countries.remove('Peru')
 countries.remove('Peru')
 print "=" * 20
 for i in countries:
  print i

 print "=" *30
 string=countries.pop(1)
 print string
 print "=" *30
 for i in countries:
  print i
 
 print "=" * 40
 countries.reverse() 
 for i in countries:
  print i
 
 print "=" * 40
 countries.insert(1,'Germany')
 for i in countries:
  print i
 print countries

 print countries[:-1]

 print "=" * 40
 countries[:-2]=['Japan']
 print countries

 countries.append('Albany') 
 print "=" * 40
 countries.sort()
 print countries

if __name__ == '__main__':
 main()
  

