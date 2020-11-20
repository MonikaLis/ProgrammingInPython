import numpy as np

matrix1 = np.random.randint(1,10,(8,8))
matrix2 = np.random.randint(1,10,(8,8))
res = [[0 for x in range(8)] for y in range(8)] 

# iterate through rows of matrix1
for i in range(len(matrix1)):
   # iterate through columns of matrix2
   for j in range(len(matrix2[0])):
       # iterate through rows of matrix2
       for k in range(len(matrix2)):
           res[i][j] += matrix1[i][k] * matrix2[k][j]

# iterate through rows
for i in range(len(res)):
   # iterate through columns
    #for j in range(len(res[0])):
        print('{}'.format(res[i]))