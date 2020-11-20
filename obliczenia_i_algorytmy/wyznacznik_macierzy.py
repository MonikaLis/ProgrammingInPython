import numpy as np
from scipy import linalg
import random

import numpy as np
from scipy import linalg

def determinant(a):
    assert len(a.shape) == 2 # check if a is a two diamentional matrix
    assert a.shape[0] == a.shape[1] # check if matrix is square
    n = a.shape[0]
   
    for k in range(0, n-1):
       
        for i in range(k+1, n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n]

               
    # the matrix (a) is now in the upper triangular form
                
    return np.prod(np.diag(a))

#matrix = np.random.rand(50, 50)
size = random.randint(2,5)
matrix = np.random.randint(1,20,(size,size))


print(linalg.det(matrix))
print(determinant(matrix))