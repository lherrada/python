class E(object):
 __slots__ = ['c','d']

class D(E):
 __slots__ = ['a','__dict__']

if __name__ == '__main__':
 d=D()
 d.a=20
 d.b=30
 d.c=40
 d.d=50
 d.e=60
 
 print d.__dict__
 print d.__slots__
 print D.__slots__
 print E.__slots__
