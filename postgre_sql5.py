# perform delete operation in the table company
import psycopg2
conn= psycopg2.connect(database="MyDatabase",user="postgres",password="mysql",host="127.0.0.1",port="5432")
print("open Database successfully :)")

cur=conn.cursor()

cur.execute("Delete from company where id=102") #delete the record whose id =102

conn.commit() #save all the changes

print("The total no. of rows deleted: ",cur.rowcount)

cur.execute ("select * from company") # select all the values from the table company

rows= cur.fetchall() # fetch all the values of the table 

for row in rows:  # iterate through all the values of the table
    print ("Id :",row[0])
    print("Name: ",row[1])
    print("Age: ",row[2])
    print("Address: ",row[3])
    print("Salary :",row[4])

print("Operation done successfully :)")
conn.close()