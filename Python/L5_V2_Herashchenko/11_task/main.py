import sympy as sp

x = sp.symbols('x')

f = x * sp.sin(x)

integral_result = sp.integrate(f, (x, 0, sp.pi))

print(integral_result)