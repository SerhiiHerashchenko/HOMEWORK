import numpy as np
import sympy as sp

# ------------------ Trapezoidal Rule ------------------

def Trapezoidal_cubature_rule(f, a, A, b, B, n, m):
    h, k = (A - a) / n, (B - b) / m
    x = a
    y = b
    integral = 0
    w = 1
    for i in range(int(n) + 1):
        y = b
        for j in range(int(m) + 1):
            if (i > 0) & (i < n) & (j > 0) & (j < m) : w = 1
            elif (i==0 | i==n ) & (j==0 | j==m) : w = 0.25
            else : w = 0.5
            integral += w * f(x, y)
            y += k
        x += h

    integral *= (h * k)
    return integral

# ------------------ My Integral ------------------

eps = 0.001

f = lambda x, y: 2 * x * sp.sin(x * y)

a, A = 0, 1
b, B = 0, sp.pi / 2

n, m = 3, 3

alg_precision = 1

print("n =", n)
print("m =", m)

result_n = Trapezoidal_cubature_rule(f, a, A, b, B, n, m)
result_2n = Trapezoidal_cubature_rule(f, a, A, b, B, n * 2, m * 2)

E = abs(result_n - result_2n) / (2**alg_precision - 1)
print("Error:", E.evalf())

# ------------------ Runge Accuracy Control ------------------
while E >= eps:
    n, m = 2 * n, 2 * m
    result_n = result_2n
    result_2n = Trapezoidal_cubature_rule(f, a, A, b, B, n * 2, m * 2)
    E = abs(result_n - result_2n) / (2**alg_precision - 1)
    print("n =", n)
    print("m =", m)
    print("Error:", E.evalf())

print("Trapezoidal rule (h):", round(result_n, 4))

x, y = sp.symbols('x y')

exact_result = sp.integrate(f(x, y), (y, 0, sp.pi / 2), (x, 0, 1))
print("Reference (sympy):", exact_result.evalf())