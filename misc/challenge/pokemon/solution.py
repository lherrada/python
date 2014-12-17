#!/usr/bin/python2.7

from collections import defaultdict

pokemon = '''audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'''

def order_words(words):
 byfirst=defaultdict(set)
 for word in words:
  byfirst[word[0]].add(word)
 return byfirst


def linkfirst(byfirst,sofar):

 chmatch = sofar[-1][-1] 
 options = byfirst[chmatch] - set(sofar)

 if not options:
  return sofar
 else:
  alternatives = ( linkfirst(byfirst,list(sofar) + [word])
 		  for word in options )
  mx = max(alternatives,key=len)
  return mx
                    
pokemon=pokemon.strip().lower().split()
pokemon=sorted(set(pokemon))

byfirst=order_words(pokemon)
#print byfirst
#initial=['rufflet']
#initial=['kricketune']

#l=linkfirst(byfirst,initial)

l=max( [ linkfirst(byfirst,[word]) for word in pokemon],key=len)
print l

for i in range(0, len(l), 8): print(' '.join(l[i:i+8]))
print(len(l))

#byfirst=order_words(pokemon)
#print byfirst['bq'] 
#sofar=['wingull']
#chmatch=sofar[-1][-1]
#print "-->",chmatch
#options=byfirst[chmatch] - set(sofar)
#print options
#print "---> ",list(sofar)
#for words in options:
# arg2= list(sofar)+ [words]
# print arg2[-1][-1]
#print order_words(pokemon).items()
#print type(order_words(pokemon))
#print type(pokemon)
#print pokemon
