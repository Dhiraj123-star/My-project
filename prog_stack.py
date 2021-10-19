#implementation of list as stack
s=[]
c='y'
while(c=='y'):
    print("1.push")
    print("2.pop")
    print("3.display")
    choice=int(input("enter your choice:"))
    if(choice==1):
        a=input("enter a number:")
        s.append(a)
    elif(choice==2):
        if(s==[]):
            print("stack empty")
        else:
            print("deleted element is:",s.pop())
    elif(choice==3):
        l=len(s)
        for i in range(l-1,-1,-1):
            print(s[i])
    else:
        print("wrong input")
    c=input("do you want to continue or not?")
