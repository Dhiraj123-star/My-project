# filter example using Python

# function that are filters vowel

def fun(var):
    letters = ['a','e','i','o','u']
    return True if var in letters else False


str = list('Dhiraj loves Python')

filtered = filter(fun,str)

print(tuple(filtered))


# another example 

seq =[1,2,5,7,90,100]

result = filter(lambda x:x%2==0,seq)

print("The even number in the list: ", list(result))


# another example

seq =[83,12,5,90,130,211]

result = filter(lambda x: x%2!=0,seq)

print("The odd numbers in the list: ",list(result))