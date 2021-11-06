# temperature convertor using Python

def celsius():
    celsius= float(input("Enter your temperature in celsius: "))
    fahrenheit= (celsius*9/5)+32
    return fahrenheit

def fahrenheit():
    fahrenheit= float(input("Enter temperature in fahrenheit: "))
    celsius=(fahrenheit-32)*5/9
    return celsius


# main program

print("1: celsius to fahrennheit------")
print("2: fahrenheit to celsius-------")

choice = int(input ("Enter your choice: "))

if choice==1:
    res=celsius()

else:
    
    res=fahrenheit()

print("Your result is: ",res)