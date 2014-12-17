import re
from operator import itemgetter

def f_decor(func):
 def wrapper(*args):
  gender={'M':'Mr','F':'Mrs'}
  myfile=args[0]
  orig=func(myfile)
  orig=sorted(orig,key=itemgetter(3,0)) 
  orig=["%s %s %s"% (gender[i[4]],i[1],i[2]) for i in orig]      
  return orig
 return wrapper
 
@f_decor
def f_orig(myfile):
 records=[]
 num=myfile.readline()
 num=num.strip()
 i=0
 for line in myfile:
  line=line.strip()
  #x=re.split('\s+',line) 	 	
  x=line.split() 	 	
  x[2]=int(x[2])
  x.insert(0,i)
  x=tuple(x)
  i+=1
  records.append(x) 
 #print records
 return records
 #print list(enumerate(records)) 

def process(records):
 gender={'M':'Mr','F':'Mrs'}
 return sorted(records,key=itemgetter(3,0))
 
def lhm(message):
 return "==> "+message+" <=="

def lhm_decor(func):
 def wrapped(*args):
  message=args[0].upper() 
  return func(message) 
 return wrapped   

if __name__ == '__main__':
 try:
  myfile=open('data1.txt')
 except Exception as e:
  print e

 records=f_orig(myfile)
 print records

#sorted_records=process(records)
#print sorted_records
#for i in sorted_records:
# print gender[i[4]],i[1],i[2]




