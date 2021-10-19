#to claculate the sum of the digits of a random three digit number
from random import random
n=random() *900 +100
n=int(n)
print(n)
a=n//100
b=(n//10)%10
c=n%10
print(a+b+c)
