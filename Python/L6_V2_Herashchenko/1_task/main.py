import numpy as np
from scipy.integrate import quad

def func(x):
    return x * np.log(x)

result_quad, error_quad = quad(func, 0, 1)

import sympy as sp
x = sp.symbols('x')
integral_sympy = sp.integrate(x * sp.ln(x), (x, 0, 1))

def transformed_func(t):
    return -np.exp(-2 * t) * t
result_transformed, error_transformed = quad(transformed_func, 0, np.inf)

print(f"quad: res = {result_quad}, error = {error_quad}")
print(f"sp.integrate: {integral_sympy.evalf()}")
print(f"quad(transformed_func): res = {result_transformed}, error = {error_transformed}")
