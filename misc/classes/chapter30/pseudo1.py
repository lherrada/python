class C1:
 def method1(self): self.__X = 88
 def method2(self): print self.__X

 #def method1(self): self.X = 88
 #def method2(self): print self.X

class C2:
 def methoda(self): self.__X = 99
 def methodb(self): print self.__X

 #def methoda(self): self.X = 99
 #def methodb(self): print self.X

class C3(C1,C2): pass

if __name__ == '__main__' :
 I=C3()
 
 I.method1(); I.methoda()
 print I.__dict__
 
 print '--> ',I._C2__X
  
 
