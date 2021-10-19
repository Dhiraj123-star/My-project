# creating pattern with numbers

def pattern(n):
    for i in range(0,n):
        for  j in range(1,i+2):
            print(j,end=" ")
        print()

    for i in range(n,0,-1):
        for j in range(i-1,0,-1):
            print(j,end=" ")
        print()

myint = int(input("Enter your number for which you want in your pattern: "))

# calling the function
pattern(myint)