def count(myclass):
 myclass.num=0
 return myclass

@count
class Spam:
 num=0 
 def __init__(self): 
  self.__class__.num+=1 
  self.name="LHM"  

 def counting(self): return self.__class__.num

@count
class Sub(Spam) :pass

@count 
class Other(Spam):pass
 

#Spam=count(Spam)

if __name__ == '__main__':

 x=Spam()
 y=Spam()
 z=Spam()
 z=Spam()
 
 print z.counting()
 #print Spam.__dict__

 print "-" * 30
 a=Sub()
 b=Sub()
 c=Sub()
 print a.counting()
 #print a.__dict__ 

 o=Other()
 p=Other()
 q=Other()
 print q.counting()
