import numpy as np
from scipy.integrate import quad

# Функция для интегрирования
def func(x):
    return x * np.log(x)

# 1. Стандартное численное интегрирование с quad
result_quad, error_quad = quad(func, 0, 1)

# 2. Символический метод (с использованием SymPy)
import sympy as sp
x = sp.symbols('x')
integral_sympy = sp.integrate(x * sp.ln(x), (x, 0, 1))

# 3. Численный метод через замену переменной
# t = -log(x) => x = exp(-t), dx = -exp(-t)dt
def transformed_func(t):
    return -np.exp(-2 * t) * t  # После подстановки в формулу
result_transformed, error_transformed = quad(transformed_func, 0, np.inf)

# Вывод результатов
print(f"Метод quad: результат = {result_quad}, погрешность = {error_quad}")
print(f"Символический результат: {integral_sympy.evalf()}")
print(f"Метод замены переменной: результат = {result_transformed}, погрешность = {error_transformed}")
