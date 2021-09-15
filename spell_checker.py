# spell checker in python

from textblob import TextBlob

mylist = ["incorect","spellin"]

corrected_list = [ ]
for word in mylist:
    corrected_list.append(TextBlob(word))

print("Incorrected words are :")

for i in mylist:
    print(i,end=" ")

print() # for new line

print("Corrected list words are: ")

for word in corrected_list:
    print(word.correct(),end= " ")

