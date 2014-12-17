class A:
 def __init__(self,A):
  self.a=10
  self._a=A

class B:
 def __init__(self,B):
  self.a=20
  self._a=B

class C(B,A):
 pass

x=C("Lurhs")

print dir(x)
print x.__dict__


#x=A("Herrada")
#print dir(x)
#print x.a
#print x._a
