#!/usr/bin/python


dict1={'Luis': 37, 'Silvia': 28, 'Leslie': 30, 'Melissa': 28, 'Eliza': 37,'Esteban':30,'Yenny':37}

dict2={}

#for i in sorted(dict1,key=dict1.__getitem__,reverse=True):
 #dict2[dict1[i]]=[]
 #dict2[dict1[i]]=[i]  

for i in sorted(dict1,key=dict1.__getitem__,reverse=True):
 if dict1[i] not in dict2: 
  dict2[dict1[i]]=[]
  dict2[dict1[i]].append(i)
 else:
  dict2[dict1[i]].append(i)


for i in sorted(dict2):
 dict2[i].sort()
 print "%d: %s" % (i,dict2[i])

# if dict2[dict1[i]]:
# dict2[str(dict1[i])]=[i]+dict2[str(dict1[i])]
 #else:
 # dict2[dict1[i]]=[]
 # dict2[dict1[i]]=[i]+dict2[dict1[i]]
 
#print dict2




# print "%s: %d" % (i,dict1[i])
