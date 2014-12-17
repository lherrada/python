class A:
 a=20
 def __init__(self,name):
  self.name=name

 def message(self):
  print self.a


if __name__ == '__main__':
 a=A('Luis')
 a.message()
