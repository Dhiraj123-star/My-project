# create table
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

#create table
cur.execute("create table student (id int, name varchar (255) ,age int );")
conn.commit()
print("Created table successfully")
# closing the connection
conn.close()