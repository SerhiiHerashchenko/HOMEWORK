import numpy as np

matrix = np.matrix([[1, -1, 3, -2, 1, -1]] * 6)

print(matrix)

s = np.sum(np.abs(matrix))

print(s)
