class c1:
 def __init__(self):
  self.__country="Peru" 
 def __fetchname(self):
  return self.__country

if __name__ == '__main__':
 x=c1()
 print x.__dict__
 print dir(x)

 print "--->",x._c1__country
