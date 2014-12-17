def classtree(classes,n):
 n+=4
 print "%s %s" % ("." * n, classes.__name__) 
 for myclass in classes.__bases__:
  classtree(myclass,n)

def classobj(obj):
 classtree(obj.__class__,0)

class F:pass
class E(F):pass
class C(E):pass
class D:pass
class A(C,D):pass
class B:pass
class obj(A,B):pass


if __name__ == '__main__':
 myobj=obj()
 
#print myobj.__class__  
 classobj(myobj)

