#!/usr/bin/python

phrase="The long grass rustled at her feet as the White Rabbit hurried"
phrase=phrase.split()

list1=map(len,phrase)
print list1

list2=[len(i) for i in phrase]
print list2

list3=[]
for i in phrase:
 list3.append(len(i)) 

print list3
