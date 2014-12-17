class gather():
 def gatherattr(self,obj):
  for i in sorted(obj.__dict__): 
   print "%s: %s" % (i,getattr(obj,i))

class X():pass

if __name__ == '__main__':
 x=X()
 x.name="Luis"
 x.copine="Carolina"
 x.country="Canada"

 y=gather() 
 y.gatherattr(x)

 gather.gatherattr(y,x)
 
 print "-" * 30 
 print gather
 print gather.__name__

