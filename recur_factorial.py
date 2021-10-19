#function to find the factorial of a number using recursion

def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)

num=int(input("enter a number:"))
if num<0:
    print("sorry ,factorial for a negative number does not exist:")
elif num==0:
    print("the factorial of 0 is 1")

else:
    print("the factorial of",num,"is",recur_factorial(num))
