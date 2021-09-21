# select details from table
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
    cur.execute("select * from student")
except mariadb.Error as e:
    print("Error",e)

print() # for new line

print("The whole details :)\n")

for id,name,age in cur:
    print("id",id)
    print("name",name)
    print("age",age)
    print() # for new line

print("Thanks for using Python + MariaDb :)")
conn.close()