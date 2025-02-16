import numpy as np
import sympy as sp
# ------------------ Gauss Quadrature for Double Integrals ------------------
def Gauss_Quadrature_2d(f, a, A, b, B, n):
    print(n)
    roots = []
    weights = []

    if n == 5:
        roots = [-0.906179845938664, -0.538469310105683, 0, 0.538469310105683, 0.906179845938664]
        weights = [0.236926885056189, 0.478628670499366, 0.568888888888889, 0.478628670499366, 0.236926885056189]
    elif n == 4:
        roots = [-0.861136311594053, -0.339981043584856, 0.339981043584856, 0.861136311594053]
        weights = [0.3478548451374529, 0.6521451548625463, 0.6521451548625463, 0.3478548451374529]
    elif n == 3:
        roots = [-0.774596669241483, 0, 0.774596669241483]
        weights = [0.555555555555556, 0.888888888888889, 0.555555555555556]
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

result_h = Gauss_Quadrature_2d(f, a, A, b, B, n)
result_2h = Gauss_Quadrature_2d(f, a, A, b, B, int(n / 2))

E = abs(result_h - result_2h) / (2**(alg_presicion) - 1)
print("Error:", E.evalf())

# ------------------ Runge Accuracy Control ------------------
while E >= eps:
    n = 2 * n
    result_h = Gauss_Quadrature_2d(f, a, A, b, B, n)
    result_2h = Gauss_Quadrature_2d(f, a, A, b, B, int(n / 2))
    E = abs(result_h - result_2h) / (2**(alg_presicion) - 1)
    print("n =", n)
    print("Error:", E.evalf())

print("Gauss quadrature formula(h):", round(result_h.evalf(), 4))

x, y = sp.symbols('x y')
exact_result = sp.integrate(f(x, y), (x, a, A), (y, b, B))
print("Reference(sympy):", exact_result.evalf())