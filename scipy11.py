# sparse array which contains maximum numbers of zeros
 
import numpy as np

from scipy.sparse import csr_matrix

arr = np.array([0,0,0,1,3,0,0,3])

print(csr_matrix(arr))