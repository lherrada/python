class Myerror(Exception):
 def __init__(self,value):
  self.value=value

 def __str__(self):
  return repr(self.value)

if __name__ == '__main__':

 try:
  raise Myerror(5)
 except Myerror as e:
  print 'My Error ocurred, value = ',e.value
