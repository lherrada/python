#!/usr/bin/python
#from pets import Pet
#from pets import Pet,Dog
from pets import * 

Bobby=Dog("Bobby",True)
Prince=Dog("Principe",False)
Chippy=Dog("Chippy",False)
Lazzy=Pet("Lazzy",'dog')

if isinstance(Bobby,Pet):
 print "Bobby is a instance of Pet"

print Bobby

if Prince.chasesCats() == True:
 print "Prince chases cats wildly!!!"
elif Prince.chasesCats() == False:
  print "Prince es un lindo perrito"


print "Name is",Chippy.getName()
print "Species is",Chippy.getSpecies()

print Chippy








