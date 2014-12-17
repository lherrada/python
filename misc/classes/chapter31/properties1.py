class property(object):
 def getage(self):
  return 40
 def setage(self,value):
  print 'Setting age:',value
  self._age=value 

 age=property(getage,setage,None,'Documenting age')

if __name__ == '__main__':
 x=property() 
 print x.age

 x.age=30 
 print x.age
 
 x.name='Luis'
 print x.name

 print x._age
 
