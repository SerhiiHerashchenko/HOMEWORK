import numpy as np
import scipy.linalg as linalg

# Матрица A и вектор B
A = np.array([[3, -2], [5, 1], [2, 0]])
B = np.array([1, 1, 1])

# 1. Метод наименьших квадратов через numpy.linalg.lstsq
x1, resids, rank, s = np.linalg.lstsq(A, B, rcond=None)
print("Решение с использованием метода наименьших квадратов (numpy.linalg.lstsq):", x1)

# 2. Метод псевдообратной матрицы через numpy.linalg.pinv
x2 = np.dot(np.linalg.pinv(A), B)
print("Решение с использованием псевдообратной матрицы (numpy.linalg.pinv):", x2)

# 3. Метод нормального уравнения (A^T * A) * x = A^T * B
x3 = np.dot(np.linalg.inv(np.dot(A.T, A)), np.dot(A.T, B))
print("Решение через нормальное уравнение:", x3)

# 4. Метод сингулярного разложения (SVD)
U, S, Vt = np.linalg.svd(A, full_matrices=False)
S_inv = np.diag(1 / S)
x4 = np.dot(Vt.T, np.dot(S_inv, np.dot(U.T, B)))
print("Решение через сингулярное разложение (SVD):", x4)
