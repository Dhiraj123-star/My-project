#program to add,delete and display the records of an employee using list implementation through stack
employee=[]
c='y'
while(c=='y'):
    print("1.push")
    print("2.pop")
    print("3.display")
    choice=int(input("enter your choice:"))
    if (choice==1):
        e_id=input("enter employee number:")
        ename=input("enter the name of employee:")
        emp=(e_id,ename)
        employee.append(emp)
    elif (choice==2):
        if (employee==[]):
            print("stack empty")
        else:
            e_id,ename=employee.pop()
            print("the deleted element is :",e_id,ename)
    elif(choice==3):
        i=len(employee)
        while i>0:
            print(employee[i-1])
            i=i-1
    else:
        print("wrong input")
    c=input("do you want to continue or not?:")
