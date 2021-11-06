def string_test(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
    print("No. of upper case letters: ",d["UPPER_CASE"])
    print("No. of lower case letters: ",d["LOWER_CASE"])

    
