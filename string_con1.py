# python program to convert a list to string

# function to convert

def listToString(arr):
    # intialise an empty string
    str1=""
    # traverse in the string

    for elem  in arr:
        str1+=elem

    return str1

# main program

myarray=[" array "," to ","string ","conversion"]

print(listToString(myarray))