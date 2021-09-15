import numpy as np

a =np.array([(1,2,3,4),(3,4,5,7)])

print(a[0,3])  # returns 2 element of 0th index i.e 3

print(a[0:,2]) # returns 2 element from 0th index to end index in this case 1th index i.e 3 and 5

print() # for new line

b= np.array([(1,2,4),(3,5,7),(10,30,45)])

print(b[0:2, 1]) # returns first element from index 0 to 1 excluding 2 i.e (2 and 5)
