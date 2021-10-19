# dice roll convertor using Python

import random
while True:
    print("1. Roll the dice \t 2. Exit")

    user= int(input("Enter your choice: "))

    if (user==1):
        number = random.randint(1,6)
        print("Your number is: ", number)
    else:
        break


print("Thanks for using Python Programming language !!!!")