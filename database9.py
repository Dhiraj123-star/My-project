# delete the table
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
    cur.execute("drop table student")
    # delete the whole table
except mariadb.Error as e:
    print("Error",e)
conn.commit() # save all the changes

print("Table deleted successfully :)")

#closing the connection
conn.close()