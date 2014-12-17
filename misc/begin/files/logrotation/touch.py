#!/usr/bin/python

for i in range(1,10):
 log='message.'+str('00')+str(i)
 #print log 
 f=open(log,'w')
 f.write(str(i)+'\n')
 f.close()

for i in range(10,100):
 log='message.'+str('0')+str(i)
 f=open(log,'w')
 f.write(str(i)+'\n')
 f.close()
# print log 

for i in range(100,1000):
 log='message.' + str(i)
 f=open(log,'w')
 f.write(str(i)+'\n')
 f.close()


