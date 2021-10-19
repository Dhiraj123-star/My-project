#arrays(list) passing to a function that calculate the arithmetic mean of the list elements
def list_avg(lst):
    l=len(lst)
    sum=0
    for i in lst:
        sum+=i
    return sum/l
print("input integers:")
a=input()
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])

avrg=list_avg(a)
print("average is:")
print(round(avrg,3))
