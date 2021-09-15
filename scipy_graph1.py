import numpy as np

from scipy.sparse.csgraph import connected_components

# scipy.sparse.csgraph for working with graph

from scipy.sparse import csr_matrix

arr = np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])

newarr = csr_matrix(arr)

print(newarr)

print(connected_components(newarr))