limit=raw_input("\nWhat is the limit? ")

ppx = 2
pn=[ppx]

limit=int(limit)
while ppx < limit:
 ppx+=1 
 for x in pn: 
  if ppx%x == 0: break
  if x == pn[-1]: pn.append(ppx) 

print pn

    
  
