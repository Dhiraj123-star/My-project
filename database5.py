# update operation in mariadb
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
    cur.execute("update student set name= 'Akash' where id=104")
    #update name where id is equal to 104
except mariadb.Error as e:
    print("Error",e)

conn.commit() # save all the updates
print("Updated records successfully")
# close the connection
conn.close()
