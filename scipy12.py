# viewing stored data(not the zero items ) with data property

import numpy as np

from scipy.sparse import  csr_matrix

arr = np.array([[0,0,0],[0,0,9],[90,0,0],[100,3,0]])

print(csr_matrix(arr).data)

# counting non-zeros with count_nonzero() method

print() # for new line

print(csr_matrix(arr).count_nonzero())

