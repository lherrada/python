#!/usr/bin/python

def main():
# names=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
 names=['Luis','Ximena','Xavier','Andrea','Patty','Xofo']
 print front_x(names)
 
 names=['apppa','clarke','karen','roncar','luis','josej','papitop']
 print match_ends(names) 

def match_ends(list):

 listame=[] 
 for i in list:
  if len(i) > 2:
   if i[0] == i[len(i)-1]:
    listame.append(i)
 
 return listame    

def front_x(names):
 listax=[]

 for i in names:
  if i[0] == 'x' or i[0] == 'X':
   listax.append(i)
 listax.sort()

 for i in listax:
  names.remove(i)
 names.sort()

 return listax + names 
 
if __name__ == '__main__':
 main()
