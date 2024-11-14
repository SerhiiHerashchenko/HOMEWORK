import sympy as sp

x = sp.symbols('x')

expr = sp.sin(sp.Abs(x)) / x

left_limit = sp.limit(expr, x, 0, dir='-')

print(left_limit)
