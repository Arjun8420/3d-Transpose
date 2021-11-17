# To find the 3D transpose of a matrix

import numpy as np

a = np.array([[[1,2,3],
               [4,5,6],
               [7,8,9]]])
b = np.array([[[1,2,3],
               [4,5,6]],
               [[0,0,0],
               [7,8,9]]])
c = np.array([[[1,2,3,4,5,],
               [6,7,8,9,10]],
               [[11,12,13,14,15],
               [16,17,18,19,20]]])

print("Transpose of a = ",np.transpose(a,axes=(2,0,1)))
print("Transpose of b = ",np.transpose(b,axes=(2,0,1)))
print("Transpose of c = ",np.transpose(c,axes=(1,0,2)))

