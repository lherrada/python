class X():
 def __init__(self,data='Herrada'):
  self.data=data

 def display(self):
  print "Data: %s" % self.data 
 
 def __str__(self):
  return "--> %s" % self.data


if __name__ == '__main__':
 a=X('Luis')
 a.display()
 print a
  
 print dir(X) 
 
