import numpy as np

a = np.array([(1,3,5), (10,45,67),(100,5,90)])

print(a.ndim)  # finding the dimension of the array

# returns the size of elements in byte

print(a.itemsize) # returns 4 that means it occupies 4 bytes in the memory

# find the data types of the element of the array

print(a.dtype) # returns i32