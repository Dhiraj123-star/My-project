import pandas as pd

# read the file
data=pd.read_excel("my.xlsx")

# output the no. of rows

print("Total rows:{0}".format(len(data)))

# see the which headers are available

print(list(data))
