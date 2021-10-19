# strong password generator using python

import random
chars = 'abcdefghijklmnopqrstuvwxyz'

chars+=chars.upper()  # change into the upper case letter

nums= str(1234567890)
special_chars = '!@#$%^&*()_+'

chars+=nums+special_chars

length =8

password = " ".join(random.sample(chars,length))

print("Your strong password is: ",password)

print("Thanks for using Python programming language!!")