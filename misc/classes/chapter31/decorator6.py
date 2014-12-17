#class Person():
import sys

YELLOW='\033[93m'
RED='\033[95m'
GREEN='\033[92m'
NORMAL='\033[0m'

class Person(object):
 def __init__(self,name,age):
  self.name = name
  self.age = age

 def __str__(self):
  return "%s is %d years old" % (self.name,self.age)

class PersonDecorator(Person):
 def __init__(self,person): 
  self._person=person   

 def __getattr__(self,attr):
  return getattr(self._person,attr)
 
 def __str__(self):
  age=self._person.age
  if age < 10: color=YELLOW
  elif age <= 18: color=GREEN
  else: color=RED
  return "%s%s%s" % (color,self._person.__str__(),NORMAL)


#Person=PersonDecorator(Person)

def main():
 p=[]
 p.append(Person('Luis',7))
 p.append(Person('Silvia',36))
 p.append(Person('Leslie',18))
 p.append(Person('Melissa',28))
  
 for person in p:
  if '-c' in sys.argv:
   person = PersonDecorator(person)
  print person

# a=person.age
# print a 

if __name__ == '__main__':
 main() 
