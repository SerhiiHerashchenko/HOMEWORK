import sympy as sp
import numpy as np

x = sp.symbols('x')

def gauss_quadrature(f, a, b, n):
    legendre_polynomial = sp.legendre(n, x)
    
    # Корни многочлена Лежандра
    roots = sp.solve(legendre_polynomial, x)
    roots = [float(root) for root in roots]
    
    # Значения узлов метода Гаусса по n точкам являются корнями полинома Лежандра.
    weights = []
    for root in roots:
        # Веса для каждого корня
        weight = 2 / ((1 - root**2) * (sp.diff(legendre_polynomial, x).subs(x, root))**2)
        weights.append(float(weight))
    
    # Преобразуем корни и веса для интервала [a; b] в [-1; 1]
    roots_transformed = [0.5 * (root + 1) * (b - a) + a for root in roots]
    weights_transformed = [0.5 * weight * (b - a) for weight in weights]
    
    # Квадратурная формула Гаусса
    integral = sum(weights_transformed[i] * f(roots_transformed[i]) for i in range(n))
    return integral

n = 5
degree = 2 * n - 1
f = lambda x: x**degree + 8*x**(degree - 2) - 5*x + 6
a = 0
b = 1
    
gauss_result = gauss_quadrature(f, a, b, n)
print(f"Квадратурна формула Гауса: {gauss_result}")
exact_result = sp.integrate(f(x), (x, a, b))
print("Sympy:", exact_result)
print("Перевірка:", np.isclose(gauss_result, float(exact_result)))