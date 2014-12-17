def classtree(cls,indent):
 print "." * indent + cls.__name__
 for supercls in cls.__bases__:
  classtree(supercls,indent+3)

def instancetree(inst):
 print "Tree of %s" % inst
 classtree(inst.__class__,3)


def selftest():
 class A: pass
 class B(A): pass
 class C: pass
 class D(B,C): pass
 class E(B,D): pass
 class F(B): pass
 
 instancetree(E()) 

if __name__ == '__main__': selftest()
