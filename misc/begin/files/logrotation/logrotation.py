#!/usr/bin/python
import os

myfile='message.'
os.rename(myfile+'009','tmp1')
os.rename(myfile+'099','tmp2')
os.rename(myfile+'999','tmp3')

range1=range(1,9)
range1.reverse()
for i in range1:
 os.rename(myfile + '00' + str(i),myfile + '00' + str(i+1)) 

range1=range(10,99)
range1.reverse()
for i in range1:
 os.rename(myfile + '0' + str(i),myfile + '0' + str(i+1)) 

range1=range(100,999)
range1.reverse()
for i in range1:
 os.rename(myfile+str(i),myfile+str(i+1)) 


os.rename('tmp1',myfile+'010')
os.rename('tmp2',myfile+'100')
os.rename('tmp3',myfile+'1000')

print "Renaming Done Successfully"
