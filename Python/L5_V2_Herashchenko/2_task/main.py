import sympy as sp

# Определяем переменную
x = sp.symbols('x')

# Задаём уравнение sin^4(x) - cos^4(x) = 0.5
equation = sp.sin(x)**4 - sp.cos(x)**4 - 0.5

# Решаем уравнение
solutions = sp.solve(equation, x)

# Выводим решения
print("Решения уравнения sin^4(x) - cos^4(x) = 0.5:")
for sol in solutions:
    print(sol)
