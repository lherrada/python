class call1:
 def __init__(self,name='luis'):
  self.name=name 

 def __call__(self,adding=" default"):
  return self.name + adding.upper()
 
 def __bool__(self):
  if self.name =='luis':
   return True
  else:
   return False

if __name__ == "__main__":
 c=call1("silvia")
 print c(" herrada") 
 print c(" valencia")
 print c()
 
 print c.__dict__ 
 if c: print "HEYYY"
