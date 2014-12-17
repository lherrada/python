#!/usr/bin/python

pokemon= "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"

def init_hash(myhash):

 pokemon1=pokemon
 alphabet=list(map(chr, range(97, 123)))
 for i in alphabet:
  myhash[i]=[]
 
 numbers=range(0,10)
 for i in numbers:
  myhash[str(i)]=[]
  
 pokemon1=pokemon1.split(' ')
 for init in pokemon1:
  char1=init[0]
  myhash[char1].append(init)

myhash={}
mypokemon=pokemon.split(' ')


#for word in ['poochyena','porygon2','porygonz','registeel']:
for word in mypokemon:
 init_hash(myhash)
 key=word[-1]
 print word 
 count=0 
 while(True):
  count+=1
  if not myhash[key]: break
  new=myhash[key].pop(0)
  key=new[-1]
  print new

 print "COUNT: %d" % count 
 print "=" * 10
