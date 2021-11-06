import math

# function to check whether a number is prime

def prime(n):
    for j in range(2,int(math.sqrt(n))+1):
        if n%j==0:break
    else: return True

    