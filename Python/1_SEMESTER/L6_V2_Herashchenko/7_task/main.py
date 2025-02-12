import numpy as np
import scipy.linalg as linalg

A = np.array([[5, 2, -1], [3, 0, 2], [1, -3, 6]])

spectral_norm_scipy = linalg.norm(A, ord=2)
print("scipy.linalg.norm:", spectral_norm_scipy)

A_T_A = np.dot(A.T, A)
eigenvalues = np.linalg.eigvals(A_T_A)
spectral_norm_definition = np.sqrt(np.max(eigenvalues))
print("by definition:", spectral_norm_definition)