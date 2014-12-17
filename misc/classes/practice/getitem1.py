class Set:
 def __init__(self,data):
  self.data=data
 
 def __getitem__(self,key): 
  print "Get item: %d" % key
  return self.data[key]

 def __len__(self): return len(self.data)

 def union(self,data1):
  for i in data1: 
   for j in self.data:
    print i,j

if __name__ == '__main__':

 obj1=Set(range(4,10)) 
 print obj1.__dict__
 print '-' * 20

# for i in obj1:
#  print i
 
# print '-' * 20
# for i in range(0,len(obj1)): 
#  print obj1[i]

 print '-' * 20
 obj2=Set(range(20,25))
 obj2.union([1,2])

 print '-' * 20
 obj2.union(Set([1,2,3]))
 

 
