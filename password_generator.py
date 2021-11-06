# password generator using Python

import random,string

password_length = int(input("Enter the length of the password: "))
password_characters=string.ascii_letters+string.digits+string.punctuation

password=[]

for x in range(password_length):
    password.append(random.choice(password_characters))

print(" ".join(password)) # print the password 