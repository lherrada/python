class myclass():
 @staticmethod
 def static_method1(x,y):
  print(x + y) 

 def message(data):
  print "Data"


class static():
 def static_method2(x,y):
  print(x + y) 
 static_method2 = staticmethod(static_method2)

def main():
 myclass.static_method1("Gianna","Luis") 
 static.static_method2("Leslie","Melissa")

 myclass.message("Gianna es hermosa")

if __name__ == '__main__':
 main()
 
