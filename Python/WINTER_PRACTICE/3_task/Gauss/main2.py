import numpy as np
import sympy as sp
# ------------------ Gauss Quadrature for Double Integrals ------------------
def gauss_quadrature_2d(f, a, A, b, B, n):
    print(n)
    roots = []
    weights = []

    if n == 4: 
        roots = [-0.339981043584856, 0.339981043584856, -0.861136311594053, 0.861136311594053]
        weights = [0.6521451548625463, 0.6521451548625463, 0.3478548451374529, 0.3478548451374529]
    elif n == 2:
        roots = [-0.577350269189626, 0.577350269189626]
        weights = [1, 1]
    elif n == 1:
        roots = [0]
        weights = [2]

    x_roots_transformed = []
    y_roots_transformed = []
    for root in roots:
        x_roots_transformed.append(((A - a) / 2) * root + (A + a) / 2)
        y_roots_transformed.append(((B - b) / 2) * root + (B + b) / 2)
    
    integral = 0
    for i in range(int(n)):
        for j in range(int(n)):
            integral += (weights[i] * weights[j] * f(x_roots_transformed[i], y_roots_transformed[j]))
    
    return ((A - a) / 2) * ((B - b) / 2) * integral

# ------------------ My Integral ------------------

eps = 0.001

f = lambda x, y: 2 * x * sp.sin(x * y)

a, A = 0, 1
b, B = 0, np.pi / 2

n = 2
alg_presicion = 2 * n - 1

print("n =", n)

gauss_result_h = gauss_quadrature_2d(f, a, A, b, B, n)
gauss_result_2h = gauss_quadrature_2d(f, a, A, b, B, int(n / 2))

E = abs(gauss_result_h - gauss_result_2h) / (2**(alg_presicion) - 1)
print("Error:", E.evalf())


while E >= eps:
    n = 2 * n
    gauss_result_h = gauss_quadrature_2d(f, a, A, b, B, n)
    gauss_result_2h = gauss_quadrature_2d(f, a, A, b, B, int(n / 2))
    E = abs(gauss_result_h - gauss_result_2h) / (2**(alg_presicion) - 1)
    print("Error:", E.evalf())

print("RESULT:\nGauss quadrature formula(h):", round(gauss_result_h.evalf(), 4), "\n")

x, y = sp.symbols('x y')
exact_result = sp.integrate(f(x, y), (x, a, A), (y, b, B))
print("Reference(sympy):", exact_result.evalf())