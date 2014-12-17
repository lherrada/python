data=[(1, 2,'', 3, '', ''), (3, 4, 3, 1, '', '')]

data2=[]

for x in data:
 mylist=[]
 for y in x:
  if y: mylist.append(y) 
 data2.append(tuple(mylist)) 

#print data2  

y=(2,'',3,4,'')

#print [ tuple(x for x in y if x) for y in data ]

def tupleop(y):
 m=[]
 for x in y:
  if x: m.append(x)
 return tuple(m)

print [tupleop(x) for x in data]
