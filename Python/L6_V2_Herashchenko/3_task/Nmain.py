import numpy as np
import sympy as sp
from scipy.misc import derivative

def f(x):
    return sp.cos(x)

x0 = sp.pi / 2

first_derivative = derivative(f, x0, dx=1e-6, n=1, order=3)
second_derivative = derivative(f, x0, dx=1e-6, n=2, order=5)

dx = sp.symbols('dx')

first_derivative_fd = sp.limit((f(x0 + dx) - f(x0)) / dx, dx, 0)

second_derivative_fd = sp.limit((f(x0 + dx) - 2 * f(x0) + f(x0 - dx)) / dx**2, dx, 0)

print(f"f' (scypy): {first_derivative}")
print(f"f'' (scypy): {second_derivative}")
print(f"f' (difference approximations): {first_derivative_fd}")
print(f"f'' (difference approximations): {second_derivative_fd}")
