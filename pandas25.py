import pandas as pd

df= pd.read_csv('my.csv')

# using tail () method which returns last rows of the dataframe

print(df.tail()) # it returns last 5 rows if parameter is not specified

print() # for new line

print(df.tail(3)) # returns last 3 rows

