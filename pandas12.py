# create a simple pandas series from a list

import pandas as pd

# single dimensional array

a=[12,34,45,55,66,7]

myvar = pd.Series(a) # change the array elements into the series

print(myvar)

# returns the value by its index


print() # for new line

print(myvar[1])  # returns 34