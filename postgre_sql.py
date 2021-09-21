# checking the connection to the postgreSQL 
import psycopg2
conn= psycopg2.connect(database="MyDatabase",user="postgres",password="mysql",host="127.0.0.1",port="5432")
print("open Database successfully :)")