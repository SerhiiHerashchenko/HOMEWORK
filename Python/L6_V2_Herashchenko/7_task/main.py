import numpy as np
import scipy.linalg as linalg

# Матрица A
A = np.array([[5, 2, -1], [3, 0, 2], [1, -3, 6]])

# 1. Спектральная норма через встроенную функцию scipy.linalg.norm (норма по умолчанию - спектральная)
spectral_norm_scipy = linalg.norm(A, ord=2)
print("Спектральная норма через scipy.linalg.norm:", spectral_norm_scipy)

# 2. Нахождение спектральной нормы по определению
A_T_A = np.dot(A.T, A)  # Матрица A^T * A
eigenvalues = np.linalg.eigvals(A_T_A)  # Собственные значения A^T * A
spectral_norm_definition = np.sqrt(np.max(eigenvalues))  # Корень из максимального собственного значения
print("Спектральная норма по определению:", spectral_norm_definition)