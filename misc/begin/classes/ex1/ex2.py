class Student:
  'Information about students'
  student_count=0

  def __init__(self1,name,school):
   self1.name=name
   self1.school=school
   Student.student_count +=1

  def displayCount(self1):
   print "Total number of Students: %d" % Student.student_count 

  def displayStudent(self1):
   print "Name: ",self1.name,  " School: ", self1.school 

