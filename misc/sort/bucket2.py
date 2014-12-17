#!/usr/bin/python
import random
import pdb

class Node:
 def __init__(self,key):
  self.key=key
  self.vertical=None

def insertItemBetween(first,current,last):
 first.vertical = current
 current.vertical = last

def addItemToList(nodes,val,index):
 node = Node(val)
 current = nodes[index]
 while not current.vertical == None:
  if val < current.vertical.key:
   insertItemBetween(current,node,current.vertical)
#   print("Inserted ",val, "in between")
   return
  else:
   #print current.key
   current = current.vertical

 current.vertical = node
# print("Inserted ",val, " at the end")


def main():
 maxValue=100
 length=50
 nbuckets=10
 array=list()
 for x in xrange(length):
  array.append(random.randint(0,99))

 #array=[7,6,7,7,7] 
 #print array

 
 nodes=list()

 #pdb.set_trace()
 #for x in xrange(length):
 # node=Node(0)
 # nodes.append(node)

 for x in xrange(nbuckets):
  node=Node(0)
  nodes.append(node)
 
 for x in xrange(length):
  val=array[x]
  #index=(val*length)/maxValue 
  index=val/10 
  addItemToList(nodes,val,index)
 
 newarray = list()

 #for x in range(length):
 for x in xrange(nbuckets):
  current = nodes[x]
  current = current.vertical
  while not current == None:
    newarray.append(current.key)
    current = current.vertical
 
 print "-"*20 
 print ("The sorted array")
 print newarray

if __name__ == '__main__':
 main()
