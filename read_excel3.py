# returns the columns heading

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df= pd.read_excel("my.xlsx",sheet_name="Sheet1")

print("Column heading")
print(df.columns)

print() # for new line

# printing the whole data

print("The whole data is:")
print(df)

# printing the columns data
print() # for new line



print("The data in the column name is: ")
print(df["Name"].tolist())

print() # for new line

print("The data in the column Rollno is: ")
print(df["Rollno"].tolist())
print() # for new line

print("The data in the column year is: ")
print(df["Year"].tolist())
print() # for new line





