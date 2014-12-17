class Set:
 def __init__(self,value=[]):
  self.data=[]
  self.concat(value)

 def concat(self,value):
  for x in value:
   if not x in self.data:
    self.data.append(x)

 def union(self,other):
  res = self.data[:]
  for x in other:
   if not x in res:
    res.append(x) 
  return Set(res)

 #def __len__(self): return len(self.data) 
 def __getitem__(self,key): return self.data[key]
 #def __or__(self,other): return self.union(other)
 def __repr__(self): return "--> Set" + repr(self.data)

if __name__ == '__main__':

 x=Set([2,4,6,8])
 #x.concat([1,3,5,7]) 
 print x.__dict__

 #print(x.union(Set([1,4,7])))
 print(x.union([1,4,7]))
 print "-" * 30
 print x

 
