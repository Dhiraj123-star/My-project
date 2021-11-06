# import the module
import mysql.connector

def insert(con,cur):
    # read the values to be inserted
    sid= input("Enter your id: ")
    sname=input("Enter your name: ")
    sage= input("Enter your age: ")
    smarks=input("Enter your marks: ")

    # create the insert query

    sql= "insert into student(studId,studName,studAge,studMarks)values(%s,%s,%s,%s)"
    # create list of value typed from user to insert in student table
    val =(sid,sname,sage,smarks)

    # execute query with the values
    cur.execute(sql,val)

    #commit for permanent storage in database

    con.commit()

    # display success message

    print(cur.rowcount,"Records inserted")

def update(con,cur):
    # read values to be updated
    sid= input("Enter your id: ")
    sname=input("Enter your name: ")
    sage= input("Enter your age: ")
    smarks=input("Enter your marks: ")
    
    #create update query

    sql = "update student set studName='"+sname+"' , studAge='"+sage+"',studMarks='"+smarks+"'where studId="+sid

    # execute update query on opened cursor
    cur.execute(sql)

    #commit changes to DB

    con.commit()

    # display success message

    print(cur.rowcount,"Records updated")

def delete(con,cur):
    #read the customer ID for which record to be deleted
    sid= input("Enter your id: ")

    #create delete query
    sql = "delete from student where studId= '"+sid+"'"

    #execute delete query

    cur.execute(sql)

    # commit changes to DB

    con.commit()

    # display success message

    print(cur.rowcount,"Records deleted")

def display(cur):
    # execute select statement

    cur.execute("select * from student")

    # fetch all records from table

    res= cur.fetchall()

    # print

    print("-------------------------------------------------------------")
    print("StudId    StudName        StudAge          StudMarks")
    print("-------------------------------------------------------------")

    for x in res:
        print(str(x[0])+"        "+x[1]+"              "+str(x[2])+"                 "+str(x[3]) ) # string formatting
    print("-----------------------------------------------------------------------")


# main program
def main():

    # make connection to the database using localhost, root as username, rootpassword and database name

    con= mysql.connector.connect(
        host= "localhost",
        user="root",
        passwd="rootpassword",
        database="mydemo"
    )

    # open cursor

    cur= con.cursor()
    ch=0

    #display menu until user presses 5

    while(ch<=4):
        # menu options

        print("1. INSERT")
        print("2. UPDATE")
        print("3. DELETE")
        print("4. DISPLAY")
        print("5. EXIT")

        # ask user to enter what he want to do

        ch= int(input("Enter your choice: "))
        
        #call relevant functions defined above

        if(ch==1):
            insert(con,cur)
        if(ch==2):
            update(con,cur)
        if(ch==3):
            delete(con,cur)
        if(ch==4):
            display(cur)

# call main
main()