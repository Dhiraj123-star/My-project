
# drop whole table 
import psycopg2
conn= psycopg2.connect(database="MyDatabase",user="postgres",password="mysql",host="127.0.0.1",port="5432")
print("open Database successfully :)")

cur=conn.cursor()

cur.execute("drop table company")
conn.commit()
print("table deleted successfully :)")

conn.close()