import numpy as np
import sympy as sp
from scipy.misc import derivative

# Функция f(x)
def f(x):
    return sp.cos(x)

# Точка, в которой вычисляем производные
x0 = sp.pi / 2

# 1. Использование встроенной функции для нахождения производных
first_derivative = derivative(f, x0, dx=1e-6, n=1, order=3)  # Первая производная
second_derivative = derivative(f, x0, dx=1e-6, n=2, order=5)  # Вторая производная

# Символьная переменная для разностной формулы
dx = sp.symbols('dx')

# Первая производная (центральная разностная формула)
first_derivative_fd = sp.limit((f(x0 + dx) - f(x0)) / dx, dx, 0)

# Вторая производная (центральная разностная формула)
second_derivative_fd = sp.limit((f(x0 + dx) - 2 * f(x0) + f(x0 - dx)) / dx**2, dx, 0)

# Вывод результатов
print("Первая производная:", first_derivative_fd)
print("Вторая производная:", second_derivative_fd)

# Вывод результатов
print(f"Первая производная (встроенная функция): {first_derivative}")
print(f"Вторая производная (встроенная функция): {second_derivative}")
print(f"Первая производная (разностная формула): {first_derivative_fd}")
print(f"Вторая производная (разностная формула): {second_derivative_fd}")
