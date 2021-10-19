#a function that fills a list with numbers
from random import randint

def fill_list(lst,limit_num,low,high):
    for i in range(limit_num):
        lst.append(randint(low,high))

minimum=int(input("min :"))
maximum=int(input("max:"))
n=int(input("number limit:"))
a=[]
fill_list(a,n,minimum,maximum)
print(a)
