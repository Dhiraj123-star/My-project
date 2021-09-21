# create table company in postgresql database named 'MyDatabase'

import psycopg2

conn= psycopg2.connect(database="MyDatabase",user="postgres",password="mysql",host="127.0.0.1",port="5432")

print("open Database successfully :)")

cur= conn.cursor()

cur.execute(''' create table company 
(id int primary key not null, name varchar(255),
age int not null, address varchar(255),
salary real);''')
print("table created successfully :)")

conn.commit() #save all the changes  

conn.close()
