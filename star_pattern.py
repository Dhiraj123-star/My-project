# star pattern with python

def StarTriangle(n):
    for i in range(n):
        print(" "*(n-1-i),end=" ")
        print("*"*(i*2+1))


user_input= int(input("Enter your number for which you want: "))

# passing user_input to the function

StarTriangle(user_input)

print("Thanks for using Python Programming  language!!!")