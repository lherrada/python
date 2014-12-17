class wrapper:
 def __init__(self,object):
  self.wrapped = object

 def __getattr__(self,attrname):
  print "Trace: ",attrname
  print dir(self.wrapped) 
  return getattr(self.wrapped,attrname)

if __name__ == '__main__':
 x=wrapper([1,2,3]) 
 print x.wrapped  
 print x.__dict__

 #x.wrapped.append(4)
# print x.__dict__
 
 print "-" * 40
# x.copine
 
 x.append(4)
 print x.wrapped

 print "-" * 40
 print x
