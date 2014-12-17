#!/usr/bin/python

class Student:
  'Information about students'
  student_count=0

  def __init__(self,name,school):
   self.name=name
   self.school=school
   Student.student_count +=1

  def displayCount(self):
   print "Total number of Students: %d" % Student.student_count 

  def displayStudent(self):
   print "Name: ",self.name,  " School: ", self.school 

# Creating objects
student1=Student("Luis","UNI")
student2=Student("Silvia","UPC")
student3=Student("Marita","Pacifico")

# Accessing methods
student1.displayStudent()
student2.displayStudent()
student3.displayStudent()

student1.displayCount()


print "Displaying total number of students: %d" % Student.student_count
print "Documentation: ",Student.__doc__
print "Name of the class: ", Student.__name__
print "Name of the module: ", Student.__module__
print "Class 's namespace: ", Student.__dict__


student1.age=37


if (hasattr(student1,'age')):
 print "Attribute age is: %d" % getattr(student1,'age')

