# order by clause
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
    cur.execute("select * from student order by age ")
    # order the records by age in ascending order 
except mariadb.Error as e:
    print("Error",e)

print() # for new line

for i , j,k in cur:
    print("id",i,"name",j,"age",k)
    

# closing the connection
conn.close()
print() # new line
print("thanks for using python + mariadb :)")