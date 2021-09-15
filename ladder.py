# ladder design in python


num= int(input("Enter number of sticks you want to add in the ladder: "))

for i in range(num+1):
    print("*    *")
    print("*    *")
    if i<num:
        print("******")