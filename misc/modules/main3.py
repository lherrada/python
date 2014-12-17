from imp import reload
import hello
a=reload(hello)

print a.num1
print a.lista

hello.num1=5
hello.lista[0]=233

print '-'*30
print a.num1
print a.lista
