# finding the gcd of a number using Python

n1 = int(input("Enter your first number:  "))
n2 = int(input("Enter your second number: "))

if (n1>n2):max=n1
else: max=n2

while(True):
    if(max%n1==0) and (max%n2==0):
        print(max)
        break
    max+=1


