# assert statement with try..catch

try:

    # user input 

    n= int(input("Enter your number as you wish:  "))

    # check for even number

    assert n%2==0 

    print(f"{n} is even number")

except:
    print(f"{n} is odd number") # we are handling the error with try..except 

