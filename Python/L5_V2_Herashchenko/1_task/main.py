import sympy as sp

a = sp.symbols('a')

expr = sp.root((1 - 2*a + a**2) * (a**2 - 1) * (a - 1), 4) / ((a**2 + 2*a - 3) / sp.root(a + 1, 4))

simplified_expr = sp.simplify(expr)

result = simplified_expr.subs(a, 5)

print("Упрощённое выражение:", simplified_expr)
print("Значение выражения при a = 5:", result)
