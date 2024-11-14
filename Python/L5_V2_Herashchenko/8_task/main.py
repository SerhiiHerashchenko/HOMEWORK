import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')(x)

eq = sp.Derivative(y, x, x) + y - sp.tan(x)

solution = sp.dsolve(eq)

print(solution)