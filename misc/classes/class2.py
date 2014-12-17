#!/usr/bin/python

class Third(object):
 def __init__(self,data):
  self.data=data 

 def __str__(self):
  return "Data Content: %s" % self.data

 def __add__(self,text):
  self.data+= " " + text 
  return Third(self.data)
  #return self.data
 
def uppercase(self):
 return self.data.upper()


third=Third("Herrada")
print type(third)

third + "Mateo"
print third + "Lorena" + "Salinas"

print third

print uppercase(third)

Third.uppercase=uppercase

again=Third("lorena")

print again.uppercase()

print "-" * 30

again=Third("sonia")


print Third.uppercase(again)

