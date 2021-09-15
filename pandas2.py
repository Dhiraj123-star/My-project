import pandas as pd

xyz_web= {"Day":[1,2,3,4,5,6],"Visitors":[1000,2000,3000,4000,5000,6000]}

df= pd.DataFrame(xyz_web)

print(df.head(2)) # only  returns top  two values 

print() # for new line

print(df.tail(2))  # returns bottom two values



