# generating strong random password using Python
import random
from string import digits
from string import punctuation
from string import ascii_letters

password=""

symbol = ascii_letters+digits+punctuation
secure_random= random.SystemRandom()

for i in range(20):
    password +="".join(secure_random.choice(symbol))


print(password)


