class classic:
 def __getattr__(self,name):
  if name == 'age':
   return 40
  else:
   raise AttributeError

 def __setattr__(self,name,value):
  print "Setting value",name,"to",value
  if name == 'age':
   self.__dict__['_age'] = value
  else:
   self.__dict__[ name ] = value


if __name__ == '__main__':
 a=classic()
 print a.age
 a.age=30 
 print a.age
 print a._age

 a.name='Maria Luisa'
 print a.name

