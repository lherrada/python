#!/usr/bin/python

def main():
 nephews={'Gabriel':4,'Ariana':3,'Camila':5}
 dict1={'Brazil':5,'Argentina':2,'Alemania':4}

 print sorted(nephews,key=nephews.__getitem__)
 
 print nephews.__getitem__("Gabriel")

 print nephews["Gabriel"]

 nephews.__setitem__("Lucia",0)

 print nephews["Lucia"]

 print "="*40

 for (k,v) in nephews.items():
  print k + " ==== " + str(v) 

 print "="*40
 for i in nephews.__iter__():
  print i  

 print "=="*45
 #print sorted(dict1,key=dict1.__getitem__)
 for i in sorted(dict1,key=dict1.__getitem__,reverse=True):
  print "%s:%d" % (i,dict1[i])

 print "=="*45
 for k,v in sorted(dict1.iteritems(),key=lambda (k,v): (v,k),reverse=True):
  print "%s:%d" % (k,v)  
 

if __name__ == '__main__':
 main()
