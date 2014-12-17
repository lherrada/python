#!/usr/bin/python

"""
46. An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up at least two other words. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every second letter is used will produce a four-letter word and a three-letter word. Here are two examples:

  "board": makes "bad" and "or".
  "waists": makes "wit" and "ass".

Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that goes through each word in the list and tries to make two smaller words using every second letter. The smaller words must also be members of the list. Print the words to the screen in the above fashion.

"""

myfile=open("unixdict.txt")

#Building list
list1=[]

for i in myfile:
 i=i.rstrip('\n')
 list1.append(i)  

myfile=open("unixdict.txt")

for word in myfile:
 word=word.rstrip('\n')
 word1=word[0::2]
 word2=word[1::2]

 #print "%s - %s - %s" % (word,word1,word2)
 
 if (word1 in list1
      and word2 in list1):
  print "%s: makes %s and %s" % (word,word1,word2)

 
