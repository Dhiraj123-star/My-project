# python tricks using fibonacci series

nterms = int(input("Enter your n terms: "))

n1,n2 , count = 0,1,0

if nterms<=0:
    print("Positive Integer")
elif nterms ==1:
    print("Fibonacci sequence of: ",nterms)
    print(n1)

else:
    print("Fibonacci sequence")
    while count < nterms:
        print(n1,end=" ")
        nth = n1+n2

        # updated values
        n1= n2
        n2= nth
        count+=1



# tricks 

print("Using python tricks!!! \n")
# using lambda function

fibo = lambda n:n if n<=1 else fibo(n-1) + fibo(n-2)

for i in range(10):
    fs = fibo(i)
    print(fs,end=" ")



