#!/usr/bin/python
from repaso1 import Citizen 
import myconstant
#from myconstant import * 

#print "Master: %s" % myconstant.master
print "Master: %s" % myconstant.mymaster
myconstant.master()

citizen1=Citizen('Luis','Peru')
citizen2=Citizen('Eliza','Mexico')

citizen1.displaycountry()
print citizen1.updatecountry('Canada')
citizen1.displaycountry()

print "=" * 10
citizen1.displayname()
#citizen1.message("SJPL");
#print citizen1.citizen_count


