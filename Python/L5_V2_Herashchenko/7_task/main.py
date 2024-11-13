import sympy as sp

# Определяем переменные
x, y = sp.symbols('x y')

# Определяем функцию f(x, y)
f = sp.cos(x + y) * sp.exp(x * y)

# 1. Первая частная производная по x и y
f_x = sp.diff(f, x)  # Частная производная по x
f_y = sp.diff(f, y)  # Частная производная по y

# 2. Вторая частная производная
f_xx = sp.diff(f_x, x)  # Вторая производная по x
f_yy = sp.diff(f_y, y)  # Вторая производная по y
f_xy = sp.diff(f_x, y)  # Смешанная производная по x и y
f_yx = sp.diff(f_y, x)  # Смешанная производная по y и x

# Упрощаем результаты
f_x = sp.simplify(f_x)
f_y = sp.simplify(f_y)
f_xx = sp.simplify(f_xx)
f_yy = sp.simplify(f_yy)
f_xy = sp.simplify(f_xy)
f_yx = sp.simplify(f_yx)

# Выводим результаты
print(f"Первая частная производная по x: {f_x}")
print(f"Первая частная производная по y: {f_y}")
print(f"Вторая частная производная по x: {f_xx}")
print(f"Вторая частная производная по y: {f_yy}")
print(f"Смешанная производная по x и y: {f_xy}")
print(f"Смешанная производная по y и x: {f_yx}")
