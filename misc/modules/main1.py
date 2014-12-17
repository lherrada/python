import hello

def ex1(string,lista):
 string=string.upper()
 lista.append('Herrada')

name='rossy'
lista1=['a','b']

ex1(name,lista1)

print name,lista1

#from hello import *
num1=20

'''
print '-' * 30
print hello.__package__
print hello.__name__
print hello.__doc__
print hello.__file__
'''

#for i in hello.__builtins__:
# print i

#print hello.__class__.__name__
#print hello.__class__.__bases__

print hello.num1

hello.num1=200
hello.num2=236

#print hello.num2
#print hello.lista

print '-'*30
print hello.num1
hello.lista=range(100,110)
print hello.lista

print '-'*30
import hello
print num1
print hello.num1
print hello.lista


