import numpy as np
import scipy.linalg as linalg

A = np.array([[3, -2], [5, 1], [2, 0]])
B = np.array([1, 1, 1])

x1, resids, rank, s = np.linalg.lstsq(A, B, rcond=None)
print("(numpy.linalg.lstsq):", x1)

x2 = np.dot(np.linalg.pinv(A), B)
print("(numpy.linalg.pinv):", x2)

x3 = np.dot(np.linalg.inv(np.dot(A.T, A)), np.dot(A.T, B))
print("(normal equation):", x3)

U, S, Vt = np.linalg.svd(A, full_matrices=False)
S_inv = np.linalg.inv(np.diag(S))
x4 = np.dot(Vt.T, np.dot(S_inv, np.dot(U.T, B)))
print("(SVD):", x4)
