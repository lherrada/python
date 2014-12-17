#!/usr/bin/python

def intersection(*args):
 res=[]
 for i in args[0]:
     for j in args[1:]:
         print i
         if i not in j: break
         else:
           if i not in res:
            res.append(i)
 return res        

def inter2(*args):
 res=[]
 for x in args[0]:
     for other in args[1:]:
         if x not in other: break
         else:
          res.append(x)
 return res

s1='Luis'
s2='Silvia'
s3="Leslie"
s4=["Melissa"]


#f1((s1,s2,s3,s4),(s3,s4))
#f1([s4,s1])
seq1=['Luis','Silvia']
seq2=['Leslie','Melissa']
seq3=['Luis','Leslie']
seq4=['Melissa','Silvia']
seq5=('Luis','Silvia','Leslie','Melissa')

#print intersection(seq1,seq4,seq5) 
print inter2(seq,seq5,seq4) 
