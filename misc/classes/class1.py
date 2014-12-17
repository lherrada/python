class person(object):
 "I am a person"
 def country(self,country):
  self.country=country
 
 def language(self,language):
  self.language=language

 def name(self,name):
  self.name=name


class company(object):
 "This a a general company description"
 def symbol(self,symbol):
  self.symbol=symbol


def upperword(string):
 return string.upper()

class wrapup(person,company):

 def aggregation(self,instance1,instance2):
  data={}
  for instance in [instance1,instance2]:
   for key,value in instance.__dict__.iteritems():
    #print "%s: %s" % (key,value) 
    data[key]=value
  self.data=data

