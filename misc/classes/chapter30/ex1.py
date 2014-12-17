class Stars:
 def __init__(self,name):
  self.name=name

 def __sportstars__(self): 
  print "Your star is %s" % self.name

class Sports:
 def __init__(self,sports):
  self.sports=sports

 def __message__(self):
  print "This is Soccer World Cup"
 
 def __conclusion__(self,obj):
  print obj.name + " is a star of " + self.sports

class Student:
 def __init__(self,name,univ='SJSU',years=0):
  self.name=name
  self.univ=univ
  self.years=years
  
 def __repr__(self):
  mylist=[] 
  mylist=[ "[" + i + " : " + str(getattr(self,i)) + "]"  for i in self.__dict__ ]
  mylist.insert(0,self.__class__.__name__)
  return ' , '.join(mylist) 

class Master(Student):
 def __init__(self,name,univ,faculty):
  Student.__init__(self,name,univ,5) 
  self.faculty=faculty
  self.activity1=Sports("soccer")

 def activities(self):
 # self.activity1.__message__()
  star1=Stars("Kaka")
  self.activity1.__conclusion__(star1) 


if __name__ == '__main__':
 s1=Student("Luis","UNI",5)
 #print s1

 s2=Master("Ivan","UNI","Electrical")
 #print s2

 s3=Master(univ="UPC",name="Silvia",faculty="Systems")
 print s3
 s3.activities()

   
