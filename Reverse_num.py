def reverseNum(num):
    rev=0
    while(num>0):
        mynum=num%10
        
        rev=rev*10+mynum
        num=num//10
    return rev


# main program

num=int(input("Enter Your number: "))

# calling the function

print("The reversed Number is: ",reverseNum(num))
