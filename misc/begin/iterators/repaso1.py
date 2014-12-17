class Citizen:
 "Information about citizens"
 citizen_count=0

 def __init__(self,name,country):
  self.name=name
  self.country=country
  Citizen.citizen_count+=1

 def message(self,message):
  print "This is the LHM message: %s" % message

 def displayname(self):
  print "Name is: %s" % self.name
  #Citizen.message(self,"Inside")
  self.message("Me Inside You")
 
 def displaycountry(self):
  print "Country is: %s" % self.country

 def updatecountry(self,country):
  oldcountry=self.country
  self.country=country
  return oldcountry
 
  
 

