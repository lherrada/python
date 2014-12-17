import types

class ListTree:
 def __str__(self):
  self.__visited = {}
  return '<Instance of {0},address {1}:\n{2}{3}>'.format(
   	  		self.__class__.__name__,
			id(self),
			self.__attrnames(self,0),
			self.__listclass(self.__class__,4))

 def __listclass(self,aClass,indent):
  dots = '.' * indent

  if aClass in self.__visited:
   return '\n{0}<Class {1}:, address {2}: (see Above)>\n'.format(
			dots,
			aClass.__name__,
			id(aClass))
  else:
      self.__visited[aClass] = True
      genabove = (self.__listclass(c,indent+4) for c in aClass.__bases__)
      #for i in genabove: print "===> ",i
      #print type(genabove)
	

      return '\n{0}<Class {1}, address {2}: \n{3}{4}{5}>\n'.format(
			dots,
			aClass.__name__,
			id(aClass),
			self.__attrnames(aClass,indent),
			''.join(genabove),
			dots)


 def __attrnames(self,obj,indent):
  spaces = ' ' * (indent + 4)
  result = ''
  for attr in sorted(obj.__dict__):
   if attr.startswith('__') and attr.endswith('__'):
      result += spaces + '{0}=<>\n'.format(attr)
   else:
      result += spaces + '{0}={1}\n'.format(attr,getattr(obj,attr))
  return result

#=========================================================================
class ListInherited:

 def __repr__(self):
  return '<Instance of %s, address %s:\n%s>' % (
          self.__class__.__name__,
	  id(self),
          self.__attrnames())

 def __attrnames(self):
  result='' 
  for attr in dir(self):
   if attr[:2] == '__' and attr[-2:] == '__':
    result += '\t name %s=< >\n' % attr 
   else:
    if not isinstance(getattr(self,attr),types.MethodType):
     result += '\t name %s=%s\n' % (attr,getattr(self,attr)) 
  return result
#=========================================================================

class ListInstance:
 def __str__(self):
  return '<Instance of %s, address %s:\n%s>' % (
          self.__class__.__name__,
	  id(self),
          self.__attrnames())

 def __attrnames(self):
  result=''   
  for attr in sorted(self.__dict__):
   result += '\tname %s = %s\n' % (attr,self.__dict__[attr])   
  return result
#=========================================================================

if __name__ == '__main__':

 class Super:
  superman="LHM"
  def __init__(self):
   self.data1="Katiana"
   self.data2="Lorena"

 #class Sub(Super,ListInstance): 
 #class Sub(Super,ListInherited): 
 class Sub(Super,ListTree): 
  def __init__(self):
   Super.__init__(self)
   self.data3="Salinas"
   self.data4="Angeles"
 
  def spam(self): pass

 x=Sub()
 x.name='Luis'
 x.country='Peru'
 print x
# print "-" * 30  
# print dir(x)

