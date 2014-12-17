from lister import ListTree

class A(ListTree,object):

 attr1=1

class B(A): pass

class C(A):
 attr1=2

class D(B,C):pass

if __name__ == '__main__':
 d=D()
 #print d.attr1  
 print d

