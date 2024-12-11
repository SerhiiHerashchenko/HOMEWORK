import numpy as np
import sympy as sp

# ------------------ Legendre polinomial ------------------
def legendre_poly(n, x):

    P_0 = 1
    P_1 = x
    
    if n == 0:
        return P_0
    elif n == 1:
        return P_1
    
    P_prev2 = P_0
    P_prev1 = P_1
    
    for i in range(2, n + 1):
        P_current = ((2 * i - 1) * x * P_prev1 - (i - 1) * P_prev2) / i
        P_prev2 = P_prev1
        P_prev1 = P_current
    
    return P_current

# ------------------ Gauss quadrature formula ------------------

def gauss_quadrature(f, a, b, n):
    x = sp.symbols('x')
    
    legendre_poly_expr = legendre_poly(n, x)
    
    roots = sp.solvers.solve(legendre_poly_expr, x)
    roots = [float(root) for root in roots]
    
    weights = []
    for root in roots:
        weight = 2 / ((1 - root**2) * (sp.diff(legendre_poly_expr, x).subs(x, root))**2)
        weights.append(float(weight))
    
    roots_transformed = [0.5 * (root + 1) * (b - a) + a for root in roots]
    weights_transformed = [0.5 * weight * (b - a) for weight in weights]
    
    integral = sum(weights_transformed[i] * f(roots_transformed[i]) for i in range(n))
    return integral

# ------------------ Example ------------------

n = 4
degree = 2 * n - 1
f = lambda x: x**degree + 5*x**(degree-1)-3*x**3

a = -2
b = 3
gauss_result = gauss_quadrature(f, a, b, n)
print("Gauss quadrature formula:", gauss_result)

x = sp.symbols('x')
exact_result = sp.integrate(f(x), (x, a, b))
print("Referense(sympy):", exact_result)

print("Are they the same?", np.isclose(gauss_result, float(exact_result)))