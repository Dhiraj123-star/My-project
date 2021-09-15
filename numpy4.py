import numpy as np

a=np.array([(4,5,6),(11,23,22)])

print(a)

# change rows into columns and vice versa

a=a.reshape(3,2)  #change into 3 by 2 (3 rows and 2 columns)

print(a)
