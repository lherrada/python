#!/usr/bin/python

"""
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same characters that contain the most words in them.
"""

def anagram(string):
 return "".join(sorted(b))


myfile=open('unixdict.txt')

mydict={}
words=[]

for word in myfile:
 word=word.rstrip('\n')
 list1=list(word)
 num=reduce(lambda x,y: x+y,[ord(i) for i in list1])
 
 #word="".join(sorted(word))
 if num in mydict:
  mydict[num].append(word)
 else:
  mydict[num]=[]  
  mydict[num].append(word)

print mydict


#for k in sorted(mydict,key=mydict.__getitem__,reverse=True):
#for k in sorted(mydict,key=mydict.__getitem__,reverse=True):
# print "{0}: {1}".format(k,mydict[k])
  
