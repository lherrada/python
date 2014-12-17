#!/usr/bin/python


def f1(x,y):
 x=20
 y=21

def f2(list1):
# list1[0]="Luis"
# list1[1]="Silvia"
  list1[0:2]=["Luis","Silvia"]

def multiple(x,y):
 x=10
 y=('Peru','Chile')
 return x,y


X=5
Y=6

f1(X,Y)

print X
print Y 

lista=['Melissa','Leslie']

f2(lista)
print lista

tuple1=('Brazil','Colombia')

X,tuple1=multiple(X,tuple1)

print X
print tuple1
