import numpy as np
import sympy as sp
# ------------------ Riemann midpoint method ------------------

def Riemann_midpoint_method(f, a, b, n, m, h, k):
    x = a
    y = b
    integral = 0

    for i in range(int(n)):
        y = b
        for j in range(int(m)):
            integral += f((x + (x + h)) / 2, (y + (y + k)) / 2)
            y += k
        x += h

    return h * k * integral

# ------------------ My Integral ------------------

eps = 0.001

f = lambda x, y: 2 * x * sp.sin(x * y)

a, A = 0, 1
b, B = 0, sp.pi / 2

n, m = 5, 5
h, k = (A - a) / n, (B - b) / m

alg_precision = 1

print("n =", n)
print("m =", m)

result_h = Riemann_midpoint_method(f, a, b, n, m, h, k)
result_2h = Riemann_midpoint_method(f, a, b, n * 2, m * 2, h / 2, k / 2)

E = abs(result_h - result_2h) / (2**alg_precision - 1)
print("Error:", E.evalf())

# ------------------ Runge Accuracy Control ------------------
while E >= eps:
    h, k = h / 2, k / 2
    n, m = 2 * n, 2 * m
    result_h = Riemann_midpoint_method(f, a, b, n, m, h, k)
    result_2h = Riemann_midpoint_method(f, a, b, n * 2, m * 2, h / 2, k / 2)
    E = abs(result_h - result_2h) / (2**alg_precision - 1)
    print("n =", n)
    print("m =", m)
    print("Error:", E.evalf())

print("Riemann midpoint method (h):", round(result_h, 4))

x, y = sp.symbols('x y')

exact_result = sp.integrate(f(x, y), (y, 0, sp.pi / 2), (x, 0, 1))
print("Reference (sympy):", exact_result.evalf())