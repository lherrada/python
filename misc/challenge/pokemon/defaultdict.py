#!/usr/bin/python
from collections import defaultdict

h=defaultdict(list)

h['Luis'].append('Ensenada')
h['Luis'].append('San Diego')
h['Luis'].append('Montreal')
h['Silvia'].append('Lima')


g=defaultdict(int)

g['Luis']+=1
g['Luis']+=1

print g 
