# assert statement with error message

n = int(input("Enter any number:  "))

# check condition with assert

assert n%2!=0 , f"{n} is an even number :("

print(f"{n} is an odd number !!")