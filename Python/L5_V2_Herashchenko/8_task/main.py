import sympy as sp

# Определяем переменные
x = sp.symbols('x')
y = sp.Function('y')(x)

# Определяем дифференциальное уравнение y'' + y = tg(x)
eq = sp.Derivative(y, x, x) + y - sp.tan(x)

# Решаем дифференциальное уравнение
solution = sp.dsolve(eq)

# Выводим общее решение
print(f"Общее решение дифференциального уравнения: {solution}")
