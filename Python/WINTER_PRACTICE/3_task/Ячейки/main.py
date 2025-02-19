import numpy as np
import sympy as sp

# ------------------ Riemann midpoint method ------------------
def Cell_method(f, a, A, b, B, n, m):
    h_a, h_b = (A - a) / n, (B - b) / m
    integral = 0

    for i in range(1, int(n + 1)):
        a_tmp = a + i * h_a
        A_tmp = a_tmp + h_a
        for j in range(1, int(m + 1)):
            b_tmp = b + j * h_b
            B_tmp = b_tmp + h_b

            tmp_integral = f((a_tmp + A_tmp) / 2, (b_tmp + B_tmp) / 2)
                
            integral += h_a * h_b * tmp_integral

    return integral

# ------------------ My Integral ------------------

eps = 0.001

# Используем np.sin вместо sp.sin
f_np = lambda x, y: 2 * x * np.sin(x * y)

a, A = 0, 1
b, B = 0, np.pi / 2

n, m = 5, 5
alg_precision = 1

print("n =", n)
print("m =", m)

result_n = Cell_method(f_np, a, A, b, B, n, m)
result_2n = Cell_method(f_np, a, A, b, B, n * 2, m * 2)

E = abs(result_n - result_2n) / (2**alg_precision - 1)
print("Error:", E)

# ------------------ Runge Accuracy Control ------------------
while E >= eps:
    n, m = 2 * n, 2 * m
    result_n = result_2n
    result_2n = Cell_method(f_np, a, A, b, B, n * 2, m * 2)
    E = abs(result_n - result_2n) / (2**alg_precision - 1)
    print("n =", n)
    print("m =", m)
    print("Error:", E)

print("Cell method (h):", round(result_n, 4))

# ------------------ Reference (SymPy) ------------------
x, y = sp.symbols('x y')
f_sym = 2 * x * sp.sin(x * y)
exact_result = sp.integrate(f_sym, (y, 0, sp.pi / 2), (x, 0, 1))
print("Reference (sympy):", exact_result.evalf())
