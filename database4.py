# select the details on the basis of where clause
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
    cur.execute("select name,age from student where id>104")
    # select name , age from student where id is greater than 104
except mariadb.Error as e:
    print("Error",e)
for i,j in cur:
    print("name",i)
    print("age",j)

conn.close()