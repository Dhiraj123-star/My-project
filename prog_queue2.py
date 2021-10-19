#program to add,remove and display the book details using list
#implement as a queue
library=[]
c='y'
while(c=='y'):
    print("1.insert")
    print("2.delete")
    print("3.display")
    choice=int(input("enter your choice:"))
    if (choice==1):
        book_id=input("enter book_id:")
        bname=input("enter the book's name:")
        lib=(book_id,bname)
        library.append(lib)
    elif(choice==2):
        if(library==[]):
            print("queue is empty")
        else:
            print("deleted item is:",library.pop(0))
    elif(choice==3):
        l=len(library)
        for i in range(0,l):
            print(library[i])
    else:
        print("wrong input")

    c=input("do you want to continue?:")
