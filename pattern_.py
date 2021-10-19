# pattern in Python

n=7
d=n//2+1
for x in range(1,n+1):
    for y in range(1,n+1):
        if y==n//2+1 or y==d or y==n-d+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    d+=1
