#main program importing modules
#this program allows the user to choice various geometrical calculations from a menu.this program imports the circle and rectangle modules
import circle
import rectangle
choice=0

ch='y'
#the display-menu function displays a menu
#def displaymenu():
while(ch=='y'):
    print("menu")
    print("1.area of the circle")
    print("2.circumference of a circle")
    print("3.area of a rectngle")
    print("4.perimeter of a rectangle")
    print("5.quit")
    choice=int(input("enter your choice:"))
    if(choice==1):
        radius=int(input("enter the circle's radius:"))
        print("the area is:",circle.area(radius))

    elif(choice==2):
        radius=int(input("enter the circle's radius:"))
        print("the circumference is",circle.circumference(radius))
    elif(choice==3):
        width=int(input("enter the rectangle's width:"))
        length=int(input("enter the rectangle's length:"))
        print("the areais",rectangle.area(width,length))
    elif(choice==4):
        width=int(input("enter the rectangle's width:"))
        length=int(input("enter the rectangle's length:"))
        print("the perimeter is",rectangle.perimeter(width,length))

    elif(choice==5):
        print("exiting the program..")

    else:
        print('error : invalid selection')
