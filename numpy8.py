import numpy as np

a=np.array([(1,2,4),(5,7,8)])

print(a.sum(axis=0)) # sum the all the columns if axis is 0

print(a.sum(axis=1)) # sum the all the rows if axis is 1


