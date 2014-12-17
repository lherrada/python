#!/usr/bin/python
# -*- coding: latin-1 -*-

dict1={ "merry":"god",
        "christmas":"jul",
        "and":"och",
        "happy":"gott",
        "new":"nytt",
        "year":"åi"}


phrase="Merry Christmas and Happy new year"
phrase=phrase.split()

phrase=[i.lower() for i in phrase]
print phrase

list2=map(lambda x:dict1[x],phrase)
print " ".join(list2)
