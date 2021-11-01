odd_square =[]

for  i in range(1,11):
    if i%2!=0:
        odd_square.append(i**2)
    
print(odd_square)


# using list comprehension

odd_square= [i**2 for  i in range(1,11) if  i %2!=0 ]

print(odd_square)

print("Thanks for using Python Programming Language!!")