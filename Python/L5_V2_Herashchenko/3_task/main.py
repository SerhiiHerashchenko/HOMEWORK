import sympy as sp

# Определяем переменные
x, y, z = sp.symbols('x y z')

# Задаём уравнения системы
eq1 = x + y + z - 6
eq2 = x**2 + y**2 + z**2 - 14
eq3 = x**3 + y**3 + z**3 - 36

# Решаем систему уравнений
solutions = sp.solve([eq1, eq2, eq3], (x, y, z))

# Выводим решения
print("Решения системы уравнений:")
for sol in solutions:
    print(sol)
