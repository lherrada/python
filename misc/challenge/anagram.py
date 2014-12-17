#!/usr/bin/python

"""
http://www.ling.gu.se/~lager/python_exercises.html

43.- An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same characters that contain the most words in them.
"""

def anagram(string):
 return "".join(sorted(b))


myfile=open('unixdict.txt')

mydict={}

for word in myfile:
 word=word.rstrip('\n')
 word2="".join(sorted(word))

 if word2 in mydict:
  mydict[word2].append(word)
 else:
  mydict[word2]=[]
  mydict[word2].append(word)

#print mydict
#print sorted(mydict.iteritems(),key=lambda k,v: len(v),reverse=True):

for k in sorted(mydict.iteritems(),key=lambda (k,v): len(v),reverse=True):
 print "{0} : {1}".format(len(k[1]),k[1])
 #print "{0}: {1}".format(k,mydict[k])
  
