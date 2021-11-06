# python program for converting list into the string using list comprehension

s=["we","are","buying",4,"mangoes","and",18 ,"bananas"]

 #using list comprehension

listToStr= ' '.join([str(elem)for elem in s])

print(listToStr)

