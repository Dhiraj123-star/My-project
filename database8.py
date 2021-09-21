# delete query
import mariadb
import sys
try:
           conn=mariadb.connect(
                      user="root",
                      password="maria",
                      host="127.0.0.1",
                      port =3308,
                      database="dhiraj"
                      )
except mariadb.Error as e:
           print("Error to connect",e)
           sys.exit(1)

print("Database connected successfully :)")
# get cursor
cur=conn.cursor()

try:
    cur.execute("delete from student where id=102")
    #delete the record where id is equal to 102
except mariadb.Error as e:
    print("Error",e)

conn.commit() # save the changes

print() # for new line

print("Data Deleted successfully :)\n")

print("After deletion the records \n")

try:
    cur.execute("select * from student")
    # retrieve all the records

except mariadb.Error as e:
    print("Error",e)

print() # for new line

for i,j,k in cur:
    print("id",i,"name",j,"age",k)

# closing the connection

conn.close()

