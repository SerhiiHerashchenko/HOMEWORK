import sympy as sp

x = sp.symbols('x')
m, n = sp.symbols('m n', positive = True, integer = True)

expr = (x**m - 1) / (x**n - 1)

limit_expr = sp.limit(expr, x, 1)

print(limit_expr)