import numpy as np
from scipy.integrate import dblquad
import sympy as sp

def integrand(y, x):
    return x * np.cos(y)

y_lower = lambda x: x - np.pi / 3
y_upper = lambda x: x + np.pi / 3

result_numeric, error_numeric = dblquad(integrand, 0, np.pi/2, y_lower, y_upper)

x, y = sp.symbols('x y')
integrand_symbolic = x * sp.cos(y)

inner_symbolic = sp.integrate(integrand_symbolic, (y, x - sp.pi/3, x + sp.pi/3))
analytic_integral = sp.integrate(inner_symbolic, (x, 0, sp.pi/2))

result_analytic = analytic_integral.evalf()

print(f"Numerical: {result_numeric}, error: {error_numeric}")
print(f"Analitic: {result_analytic}")
