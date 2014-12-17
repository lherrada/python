class Processor:
 def __init__(self,reader,writer,converter=None):
  self.reader=reader
  self.writer=writer
  self.myconverter=converter  

 def process(self):
  while True:  
   data=self.reader.readline()
   if not data: break
  
   if self.myconverter:
    data=self.myconverter(data)
   else:
    data=self.converter(data) 

   self.writer.write(data)

 def converter(self,data):
  assert False, 'Class ' + self.__class__.__name__ + ' must define its own converter'
  
    
 
