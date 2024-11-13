import sympy as sp

# Определяем переменную x и натуральные числа m и n
x = sp.symbols('x')
m, n = sp.symbols('m n', positive = True, integer = True)

# Формула для выражения
expr = (x**m - 1) / (x**n - 1)

# Вычисляем предел при x стремящемся к 1
limit_expr = sp.limit(expr, x, 1)

# Выводим результат
print(limit_expr)