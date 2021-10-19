# enumerate example in python

l1= ["Python","Java","C","C++","JavaScript","TypeScript"]

s1 = "Dhiraj is learning Python"

print(list(enumerate(l1)))

print()
# change start index to 10 from 0

print(list(enumerate(l1,10)))



for i in enumerate(s1):
    print(i)

print("Thanks for using Python!!")