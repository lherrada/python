#!/usr/bin/python
import class1
from class1 import upperword
from class1 import wrapup 

person1=class1.person()

person1.name="Luis"
person1.country="Peru"
person1.language="Spanish"

company1=class1.company()
company1.symbol="YHOO"

print person1.__dict__
print company1.__dict__

print upperword('herrada')

print "-"*30

aggregation1=wrapup()

aggregation1.aggregation(person1,company1)

print aggregation1.data



