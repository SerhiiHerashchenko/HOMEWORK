import numpy as np

def is_positive_definite(matrix):
    n = matrix.shape[0]

    for i in range(1, n + 1):
        minor = matrix[:i, :i]
        if np.linalg.det(minor) <= 0:
            return False
    
    return True

A = np.matrix([[22, -9, 7],
                [-9, 22, -19],
                [7, -19, 17]])

B = np.matrix([[9, 9, 2, 5, 5],
                [-4, 1, 1, 2, 8],
                [8, 7, 0, 4, 2],
                [4, -1, 9, 7, -5],
                [2, 5, 2, -4, 8]])

print(is_positive_definite(A))
print(is_positive_definite(B))