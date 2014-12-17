#state=0
def tester(start):
 #state=start
 def nested(label):
  global state
  state = 1
  print (label,state)
 return nested

if __name__ == '__main__':

 F=tester(49) 
 F('Herrada')
# print state

