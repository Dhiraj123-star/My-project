# inserting data
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
    cur.execute("insert into student values (101,'Dhiraj',22),(102,'Yasweer',23),(103, 'Gajendra',25), (104, 'Rakesh',34),(105,'Rahul',33);")
except  mariadb.Error as e:
    print("error",e)
conn.commit()
print("Data inserted successfully :)")
#closing the connection
conn.close()