import sympy as sp

# Определяем переменную x
x = sp.symbols('x')

# Определяем функцию f(x) = x * sin(x)
f = x * sp.sin(x)

# Вычисляем определённый интеграл от 0 до pi
integral_result = sp.integrate(f, (x, 0, sp.pi))

# Выводим результат
print(f"Результат интеграла: {integral_result}")
