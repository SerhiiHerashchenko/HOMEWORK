import sympy as sp

# Определяем переменную x
x = sp.symbols('x')

# Определяем выражение для функции
expr = sp.sin(sp.Abs(x)) / x

# Находим левосторонний предел при x стремящемся к 0
left_limit = sp.limit(expr, x, 0, dir='-')

print(left_limit)
