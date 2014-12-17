#!/usr/bin/python


pokemon = '''audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'''


pokemon = "audino ajeno zoozoo"

pokemon=pokemon.lower().split()

#mylist=[word for word in pokemon]
#print mylist

ord_minc = ord(min(word[0] for word in pokemon))
ord_maxc = ord(max(word[0] for word in pokemon))
sequences = [[] for _ in xrange(ord_maxc - ord_minc + 1)]

for word in pokemon:
 sequences[ord(word[0]) - ord_minc].append([word, False])

current_path = [None] * len(pokemon)
longest_path = []

for seq in sequences:
 for pair in seq: 
   


print sequences 
#print ord_minc,ord_maxc

#min1=min(word[0] for word in pokemon) 



#p=ord(min(word[0] for word in pokemon))
#ord_maxc = ord(max(word[0] for word in pokemon))

#print p
#print ord_maxc


#print type(pokemon)
