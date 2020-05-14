# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:54:08 2020

@author: ashutosh.yadav
"""

# Python program to print the similar 
# words using Enchant module 
  
# Importing the Enchant module 
import enchant 
  
# Using 'en_US' dictionary 
d = enchant.Dict("en_US") 
  
# Taking input from user 
word = input("Enter word: ") 
  
d.check(word) 
  
# Will suggest similar words 
# form given dictionary 
print(d.suggest(word))




from PyDictionary import PyDictionary

dictionary=PyDictionary('category')
print(dictionary.getMeanings())
#print (dictionary.meaning("indentation"))
print (dictionary.synonym("world"))
#print (dictionary.antonym("Life"))
