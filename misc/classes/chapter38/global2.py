def f():
 global s
 print s
 s="Silvia Herrada Mateo"
 print s.upper()

def g():
 a=10
 def h(data):
  global a
  a=a+1
  print a,data 
 h('Luis')

def p():
 a=10
 def h(data):
  global a
  a+=1
  print a,data
 return h


if __name__ == '__main__':
 s="Luis Herrada Mateo"
 f()
 print s
 print '-'*40
 a=100
 g()
 g()
 print '-'*40
 a=200
 x=p() 
 x('Luis')
 print a

 
