#!/usr/bin/python

"""Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n"""


def filter_long_words(mylist,n):
 return filter(lambda x: len(x)>n,mylist)


listA=['asasa','fdfdfd','gfgfgfgf','hghgapayaza','dsdsdsdsdsdsqqfd']
n=9

print filter_long_words(listA,n)
