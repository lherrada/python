class Eggs:
 def lhm(self,message):
  print "Message: ",message

 def m1(self,n):
  print n

 def m2(self,m):
  p=self.m1
  p(m)
  p("LHM")
 
if __name__ == '__main__':
 a=Eggs()
 print a.lhm
 p=a.lhm
 p("Oxenford")  

 print "-" * 30 
 t=Eggs.lhm
 print t
 t(a,"Erika, donde estas mi vida")
 
 print "-" * 30 
 a.m2("Relaxing Music") 
 
 Eggs().m2("Piano")
