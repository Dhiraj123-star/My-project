# filter example in python

seq=[]
limit= int(input("Enter your limit: "))

for i in range(limit):
    num=int(input("Enter your number: "))
    seq.append(num)

# result contains odd numbers from the list

result = filter(lambda x: x%2!=0,seq)

print("The odd numbers list is: ",list(result))

# result contains even numbers from the list

result= filter(lambda x: x%2==0,seq)

print("The even numbers list is" ,list(result))
