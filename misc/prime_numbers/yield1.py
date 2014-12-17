def create_generator():
 mylist=range(3)
 for i in mylist:
  yield i**2

def ex2(num):
 a=[3,34,12,34,12,34]
 i=0




x=create_generator()

print x
print "-" * 30

for i in x: 
 print i
 print i**2
