class A(object):
 __slots__=['attr1','attr2','__dict__']
 #__slots__=['attr1','attr2']
 c=20


if __name__ == '__main__':
 a=A()
 #print(dir(a))
 a.attr1=10
 a.attr2=20
 a.attr3=30
 #print list(a.__dict__)
 
 for i in list(a.__dict__) + a.__slots__:
  print (i,'=>',getattr(a,i)) 

 print "-" * 30
 print getattr(a,'__dict__')
 print getattr(a,'__slots__')

 print "-" * 30

 for attr in list(getattr(a,'__dict__')) + list(getattr(a,'__slots__')):
  print (attr,'=>',getattr(a,attr)) 
 
