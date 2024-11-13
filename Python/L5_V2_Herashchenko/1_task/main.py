import sympy as sp

# Определяем переменную
a = sp.symbols('a')

# Задаём выражение
expr = sp.root((1 - 2*a + a**2) * (a**2 - 1) * (a - 1), 4) / ((a**2 + 2*a - 3) / sp.root(a + 1, 4))

# Упрощаем выражение
simplified_expr = sp.simplify(expr)

# Вычисляем значение выражения при a = 5
result = simplified_expr.subs(a, 5)

# Выводим упрощённое выражение и результат
print("Упрощённое выражение:", simplified_expr)
print("Значение выражения при a = 5:", result)
