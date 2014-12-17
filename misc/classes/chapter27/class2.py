class Person(object):
 def __init__(self,name,lastname,company,position,age):
  self.name=name
  self.lastname=lastname
  self.company=company
  self.position=position
  self.age=age

 def __str__(self):
  return ("Category: %s\n Name: %s %s, Company: %s, Position: %s, Age: %d" %
  (self.__class__.__name__,self.name,self.lastname,self.company,self.position,self.age))

class Manager():
 def __init__(self,name,lastname,company,age):
  self.person=Person(name,lastname,company,"Manager",age)

 def __str__(self):
  return(str(self.person))

 def __getattr__(self,attr):
  return getattr(self.person,attr)


if __name__ == '__main__':
 lhm=Person('Luis','Herrada',None,None,37)
 print lhm

 ioc=Person('Ivan','Oscco','Telefonica','Analyst',39)
 print ioc 
 
 rga=Manager('Ruben','Gutierrez','Impsat',37)
 print rga

 print "-" * 40 
 jtl=Manager('Jose','Tovar','Telmex',37)
 #print jtl
 #print jtl.__dict__['person'].__dict__
 #print getattr(jtl,'name')
 #
 # Operations such as obj.attr call method __getattr__
 jtl.name="Luis"
 print jtl.name,jtl.lastname
 print jtl
 print jtl.__dict__
