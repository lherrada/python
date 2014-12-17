class Spam:
 num=0
 def __init__(self):
  Spam.num+=1
 
 @staticmethod
 def printnum():
  print "Number of instances: ",Spam.num

if __name__ == '__main__':
 for i in range(10):
  Spam()
 
 Spam.printnum()

 x=Spam()
 x.printnum()
