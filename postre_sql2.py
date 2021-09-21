
#inserting records into the table company
import psycopg2

conn= psycopg2.connect(database="MyDatabase",user="postgres",password="mysql",host="127.0.0.1",port="5432")
print("open Database successfully :)")
cur=conn.cursor()
cur.execute("Insert into company values(101,'Dhiraj',22,'Bhiwadi', 23000.7),(102, 'yasweer',23,'Rewari',3456.6),(103, 'Gajendar',25,'Gurgaon',4589.7);")
conn.commit() #save all the changes 
print("Records created successfully :)")
conn.close()