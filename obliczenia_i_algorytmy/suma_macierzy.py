import numpy as np

matrix1 = np.random.randint(1,100,(128,128))
matrix2 = np.random.randint(1,100,(128,128))
res = [[0 for x in range(128)] for y in range(128)] 
# iterate through rows
for i in range(len(matrix1)):
   # iterate through columns
   for j in range(len(matrix1[0])):
       res[i][j] = matrix1[i][j] + matrix2[i][j]

# iterate through rows
for i in range(len(res)):
   # iterate through columns
    #for j in range(len(res[0])):
        print('{}'.format(res[i]))
