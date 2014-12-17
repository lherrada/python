#!/usr/bin/python

class myiter():
 def __init__(self,data):
  self.data=data

 def __str__(self):
  return "--> " + str(self.data)

# def __iter__(self):
 # print "==> __iter__: "
 # self.count=0
 # return self

 def next(self):
  print "next: ",
  if self.count == len(self.data): raise StopIteration
  index=self.data[self.count]
  self.count+=1
  return index 

# def __contains__(self,x):
#  print "Contains: ",
#  return x in self.data
 
 def __getitem__(self,index):
  print "__getitem__ [%s]: " % index
  return self.data[index] 

#lhm=myiter("Luis")
lhm=myiter([2,4,5,3,6,9])

for i in lhm:
 print i,

print '\n' + "=" * 10
print(5 in lhm)

print "=" * 10
print lhm[2:6]

print "=" * 10
print([i ** 3 for i in lhm])



