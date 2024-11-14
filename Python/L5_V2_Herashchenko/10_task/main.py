import sympy as sp

x = sp.symbols('x')

f = x / (3 - 2 * x**2)

F = sp.integrate(f, x)

F_prime = sp.diff(F, x)

print(f"antiderivative f(x): {F}")
print(f"(d/dx(F)): {F_prime}")