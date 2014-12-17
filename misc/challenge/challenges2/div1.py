#!/usr/bin/python

list1=[]
for i in range(2000,3201):
 if i % 7 == 0 and i % 5 != 0:
  list1.append(i)

list1=[str(i) for i in list1]

print ",".join(list1)
