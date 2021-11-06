# python program for converting list into the string using join()

def listToStr(arr):
    #initialise an empty string
    str=" --"

    # returns string
    return(str.join(arr))

# main program

arr = ["Python","Java","C#","Kotlin","Scala"]

print(listToStr(arr))


