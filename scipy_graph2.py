import numpy as np

from scipy.sparse.csgraph import dijkstra

from scipy.sparse import csr_matrix

arr = np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])

newarr = csr_matrix(arr)
# find  the shortest path from element 1 to 2
print(dijkstra(newarr,return_predecessors=True,indices=0))

