#!/usr/bin/python

from collections import defaultdict 

def process(myhash,current):
 chmatch=current[-1][-1] 
 options=list(myhash[chmatch])
 #options=myhash[chmatch] - set(current)

 #print "OPTIONS: ",options
 #print "CURRENT: ",current
 
 for i in current:
  try: options.remove(i) 
  except ValueError: pass

 #print "--> ",options

 if not options:
  return current
 else:
 # alternatives = ( process(myhash,list(current) + [word])
  #                for word in options )
  #mx = max(alternatives,key=len)
  #return mx

  listA=[]
  for word in options:
   possible=process(myhash,list(current)+[word])
   listA.append(possible) 
 
  mx=max(listA,key=len) 
  return mx 

pokemon = '''audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'''


pokemon=sorted(set(pokemon.lower().split()))
myhash=defaultdict(list)

#myhash=defaultdict(set)

for word in pokemon:
 myhash[word[0]].append(word)
 #myhash[word[0]].add(word)

#pokemon=['loudred','lumineon','lunatone','audino','bagon','baltoy','banette','bidoof','braviary bronzor', 'carracosta','charmeleon']

#l=max([ process(myhash,[word]) for word in pokemon],key=len)
#print len(l)

listB=[process(myhash,[i]) for i in pokemon]
max1=max(listB,key=len)

print max1
print len(max1)
 
#print process(myhash,['simisear']) 
