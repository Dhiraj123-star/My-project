# program for write some details in the file
name=input("enter your name:")
age=input("enter your age:")
f=open("user_details.txt",'a')
f.write(name)
f.write(age)
f.close()
