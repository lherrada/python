class C:
 def __init__(self,name):
  self.__name=name

if __name__ == '__main__':
 c=C('Luis')
 print c.__dict__

