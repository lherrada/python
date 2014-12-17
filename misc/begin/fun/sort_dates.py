#!/usr/bin/python

import re
import calendar
months=[i[0:3] for i in calendar.month_name][1:]

filename="list_of_dates.txt"
dict_months=dict(zip(months,range(0,12)))

def sort_dates(mydate):
 mydate=re.split("\W+",mydate)
 mydate[0]=dict_months[mydate[0]]
 return [map(int,mydate)] 

try:
 myfile=open(filename)
except IOError as e:
 print "Error: %s" % e.strerror

#print dict_months

list_of_dates=[]
for line in myfile:
 line=line.strip()
 list_of_dates.append(line)  

for key in sorted(list_of_dates,key=sort_dates):
 print key

# mylist=re.split("\W+",line) 
# mylist[0]=dict_months[mylist[0]] 
# print mylist
 









#for i in enumerate(months):
# j=list(i)
# j.reverse()
# print j
 


