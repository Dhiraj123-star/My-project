import pandas as pd

ranking= { "Python":1,"Java":2,"C":3,"C++":4,"JavaScript":5}

# create a series using only data from C++ and Java


myvar = pd.Series(ranking,index=["C++","Java"]) 

print(myvar)

