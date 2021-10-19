#implementing list as a queue- using function pop()
a=[]
c='y'
while(c=='y'):
    print("1.insert")
    print("2.pop")
    print("3.display")
    choice=int(input("enter your choice:"))
    if(choice==1):
        b=int(input("enter new number:"))
        a.append(b)
    elif (choice==2):
        if(a==[]):
            print("queue is empty")
        else:
            print("deleted element is:",a[0])
            a.pop(0)
    elif (choice==3):
        l=len(a)
        for i in range(0,l):
            print(a[i])


    else:
        print("wrong input")
    c=input("do you want to be continue?:")
