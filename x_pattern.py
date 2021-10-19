# pattern of x in python

def x_pattern(n):
    for i in range(0,n):
        for j in range(0,n):
            if (i==j) or (j==n-1-i):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    
usr_input= int(input("Enter your number for which you want: "))
# passing argument to the function

x_pattern(usr_input)

