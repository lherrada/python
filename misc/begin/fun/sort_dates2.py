#!/usr/bin/python

import sys
import re
import calendar
months=[i[0:3] for i in calendar.month_name][1:]
dict_months=dict(zip(months,range(0,12)))

def sort_dates(mydate):
 mydate=re.split("\W+",mydate)
 mydate[0]=dict_months[mydate[0]]
 return [map(int,mydate)] 

list_of_dates=[]
for line in sys.stdin:
 line=line.strip()
 list_of_dates.append(line)    

for key in sorted(list_of_dates,key=sort_dates):
 print key
