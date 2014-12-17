class Index:
 def __init__(self,lista):
  self.lista=lista

 def __getitem__(self,index):
  if index.__class__.__name__ == 'int':
   if index>0:
    return self.lista[index-1]
   else:
    raise IndexError('Index must be greater than 0')
  elif index.__class__.__name__ == 'slice':
   if index.start>0: 
    return self.lista[index.start-1:index.stop-1]  
   else:
    raise IndexError('Lower limit must be greater than 0')
    

#@Index
a=range(1,21)
a=Index(a)

#for i in range(1,21):
# print a[i]

#print a[0]
print a[1:5]
print a[1]

print a[0:10]
