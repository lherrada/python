class C:
 def __init__(self,name='luis'):
  self.name=name

# def __nonzero__(self):
#  if self.name == 'luis': return True
#  else: return False 

 def __len__(self):
  print "Testing __len__ method"
  return 0 

class Truth:
 def __bool__(self): return False


if __name__ == '__main__':
 
 myc=C('Silvia')

 if myc: print "Heyyyyy"
 else: print "Noooooo"



# print len(myc)
