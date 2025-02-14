import numpy as np
import sympy as sp

# ------------------ Legendre Polynomial ------------------
def legendre_poly(n, x):
    P_0 = 1
    P_1 = x
    
    if n == 0:
        return P_0
    elif n == 1:
        return P_1
    
    P_prev2 = P_0
    P_prev1 = P_1
    P_current = P_0
    
    for i in range(2, int(n + 1)):
        P_current = ((2 * i - 1) * x * P_prev1 - (i - 1) * P_prev2) / i
        P_prev2 = P_prev1
        P_prev1 = P_current
    
    return P_current

# ------------------ Gauss Quadrature Formula ------------------
def gauss_quadrature_1d(f, a, b, n):
    x = sp.symbols('x')
    legendre_poly_expr = legendre_poly(n, x)
    roots = sp.solvers.solve(legendre_poly_expr, x)
    roots = [float(root) for root in roots]
    
    weights = []
    for root in roots:
        weight = 2 / ((1 - root**2) * (sp.diff(legendre_poly_expr, x).subs(x, root))**2)
        weights.append(float(weight))
    
    # Change of variables
    roots_transformed = [(b - a) / 2 * root + (b + a) / 2 for root in roots]
    weights_transformed = [(b - a) / 2 * weight for weight in weights]
    
    integral = sum(weights_transformed[i] * f(roots_transformed[i]) for i in range(n))
    return integral

# ------------------ Gauss Quadrature for Double Integrals ------------------
def gauss_quadrature_2d(f, a, A, b, B, n):
    x = sp.symbols('x')
    legendre_poly_expr = legendre_poly(n, x)
    roots = sp.solvers.solve(legendre_poly_expr, x)
    roots = [float(root) for root in roots]
    
    weights = []
    x_roots_transformed = []
    y_roots_transformed = []
    for root in roots:
        weight = 2 / ((1 - root**2) * (sp.diff(legendre_poly_expr, x).subs(x, root))**2)
        weights.append(float(weight))
        x_roots_transformed.append((A - a) / 2 * root + (A + a) / 2)
        y_roots_transformed.append((B - b) / 2 * root + (B + b) / 2)
    
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

print("Gauss quadrature formula(h):", round(gauss_result_h.evalf(), 4))
print("Gauss quadrature formula(2h):", round(gauss_result_2h.evalf(), 4))

x, y = sp.symbols('x y')
exact_result = sp.integrate(f(x, y), (x, a, A), (y, b, B))
print("Reference(sympy):", exact_result.evalf())