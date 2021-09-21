# english dictionary in python

from PyDictionary import PyDictionary

dict= PyDictionary()

spell = input("Enter your word to find out meaning: ")

meaning= dict.meaning(spell)



print(meaning)
