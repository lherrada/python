class Spam:

 def __init__(self,name):
  #self.name=self.uppername(name)  
  def uppername(name):
   return name.upper()
  self.f1=uppername

if __name__ == '__main__':
 x=Spam('luis')
 print x.__dict__

 print x.f1('melissa')
