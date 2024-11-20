import numpy as np
import scipy.linalg as linalg

# Матрица A и вектор B
A = np.array([[5, 2, -1], [3, 0, 2], [1, -3, 6]])
B = np.array([3, 2, 1])

# 1. Решение с помощью numpy.linalg.solve()
x1 = np.linalg.solve(A, B)
print("Решение с использованием numpy.linalg.solve:", x1)

# 2. Решение с помощью scipy.linalg.solve()
x2 = linalg.solve(A, B)
print("Решение с использованием scipy.linalg.solve:", x2)

# 3. Решение с помощью обратной матрицы
A_inv = np.linalg.inv(A)
x3 = np.dot(A_inv, B)
print("Решение с использованием обратной матрицы:", x3)
