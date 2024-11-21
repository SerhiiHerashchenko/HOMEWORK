import numpy as np
import scipy.linalg as linalg

A = np.array([[5, 2, -1], [3, 0, 2], [1, -3, 6]])
B = np.array([3, 2, 1])

x1 = np.linalg.solve(A, B)
print("numpy.linalg.solve:", x1)

x2 = linalg.solve(A, B)
print("scipy.linalg.solve:", x2)

A_inv = np.linalg.inv(A)
x3 = np.dot(A_inv, B)
print("inverse matrix:", x3)
