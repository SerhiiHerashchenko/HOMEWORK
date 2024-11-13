import sympy as sp

# Определяем переменные
x1, x2, x3, y1, y2, y3 = sp.symbols('x1 x2 x3 y1 y2 y3')

# Определяем функцию u(x1, x2, x3)
u = 1 / sp.sqrt((x1 - y1)**2 + (x2 - y2)**2 + (x3 - y3)**2)

# Вычисление вторых частных производных по x1, x2, x3
u_x1 = sp.diff(u, x1, 2)  # Вторая производная по x1
u_x2 = sp.diff(u, x2, 2)  # Вторая производная по x2
u_x3 = sp.diff(u, x3, 2)  # Вторая производная по x3

# Сумма вторых производных
laplacian = u_x1 + u_x2 + u_x3

# Упрощение выражения
laplacian_simplified = sp.simplify(laplacian)

# Выводим результат
print(f"Сумма вторых производных: {laplacian_simplified}")
