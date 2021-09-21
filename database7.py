# order by clause in descending order
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
    cur.execute("select * from student order by id desc")
    # ordering the records in descending order in terms of id
except mariadb.Error as e:
    print("Error",e)

print() # for new line

for i,j,k in cur:
    print("id",i,"name",j,"age",k)

print() # for new line

# closing the connection
conn.close()

