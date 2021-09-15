import pandas as pd

# reading first  six records from .csv file

# viewing the data with the help of head()

df=pd.read_csv('my.csv')

print(df.head(6))


print() # for new line

# if the number of rows is not specified , the head() method will return the top 5 rows

print(df.head())