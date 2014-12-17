class Attrdisplay:
 data="CLASS ATTR"

 def gatherattrs(self):
  mylist=[]
  for attr in self.__dict__:
   mylist.append('%s: %s' %(attr,getattr(self,attr)))   
  return ' ,'.join(mylist)

 def __str__(self):
  return "[ %s ]: %s" % (self.__class__.__name__,self.gatherattrs())

class Person(Attrdisplay):
 def __init__(self,name,lastname,company,position,age):
  self.name=name
  self.lastname=lastname
  self.company=company
  self.position=position
  self.age=age

# def __str__(self):
#  return ("Category: %s\n Name: %s %s, Company: %s, Position: %s, Age: %d" %
#  (self.__class__.__name__,self.name,self.lastname,self.company,self.position,self.age))

class Manager(Person):
 def __init__(self,name,lastname,company,age):
  Person.__init__(self,name,lastname,company,"Manager",age)

if __name__ == '__main__':
 lhm=Person('Luis','Herrada',None,None,37)
 print lhm
 print " ---> %s" % lhm.data

 ioc=Person('Ivan','Oscco','Telefonica','Analyst',39)
 print ioc 
 
 rga=Manager('Ruben','Gutierrez','Impsat',37)
 print rga

 jtl=Manager('Jose','Tovar','Telmex',37)
 print jtl
 #print jtl.__dict__['person'].__dict__
 #print getattr(jtl,'name')
 #
 # Operations such as obj.attr call method __getattr__
# jtl.name="Luis"
# print jtl.name,jtl.lastname
# print jtl
# print jtl.__dict__
