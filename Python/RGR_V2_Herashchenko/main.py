import numpy as np
from scipy.integrate import dblquad

# ---------------- Кубатуры Симпсона ----------------

def double_integral_cubature_simpson(n):
    R = 5  # Радиус окружности

    def f(x, y):
        return 1 / np.sqrt(24 + x**2 + y**2)

    # Границы интегрирования
    a, A = -R, R
    b, B = -R, R

    # Шаги разбиения
    h = (A - a) / (2 * n)
    k = (B - b) / (2 * n)

    integral = 0

    # Цикл по всем прямоугольным ячейкам
    for i in range(n):
        for j in range(n):
            # Границы текущего прямоугольника
            x0, x2 = a + 2 * i * h, a + 2 * i * h + 2 * h
            x1 = x0 + h
            y0, y2 = b + 2 * j * k, b + 2 * j * k + 2 * k
            y1 = y0 + k

            # Проверка, чтобы узлы находились внутри круга
            if x0**2 + y0**2 > R**2 or x2**2 + y2**2 > R**2:
                continue

            # Используем формулу Симпсона для текущего прямоугольника
            local_integral = (h * k / 9) * (
                f(x0, y0) + f(x2, y0) + f(x0, y2) + f(x2, y2) +
                4 * (f(x1, y0) + f(x0, y1) + f(x2, y1) + f(x1, y2)) +
                16 * f(x1, y1)
            )

            # Добавляем вклад от текущего прямоугольника
            integral += local_integral

    return integral

# ---------------- Метод Симпсона ----------------

def double_integral_simpson(n):
    
    N = 2 * n

    R = 5  # радиус окружности
    def f(x, y):
        return 1 / np.sqrt(24 + x**2 + y**2)
    
    # Внешний интеграл
    def simpson_outer(y):
        a, b = -np.sqrt(R**2 - y**2), np.sqrt(R**2 - y**2)  # границы по x
        return simpson(lambda x: f(x, y), a, b, N)
    
    # Функция Симпсона для одномерного интеграла
    def simpson(func, a, b, N):
        h = (b - a) / N  # Шаг разбиения
        x = np.linspace(a, b, N + 1)  # Узлы интегрирования
        s = func(x[0]) + func(x[-1])  # Первое и последнее значение
        s += 4 * sum(func(x[1:N:2]))  # Сумма по нечётным индексам
        s += 2 * sum(func(x[2:N-1:2]))  # Сумма по чётным индексам
        return s * h / 3
    
    # Внешний интеграл
    integral = simpson(simpson_outer, -R, R, N)
    return integral

# Проверка функций
print("Кубатурная формула:", double_integral_cubature_simpson(n=200))
print("Метод Симпсона:", double_integral_simpson(n=200))

# ---------------- Референсное значение ----------------

def f(x, y):
    return 1 / np.sqrt(24 + x**2 + y**2) # Функция под интегралом
def output(x):
    return np.sqrt(25 - x**2)  # Вычисление верхней границы по y, которая зависит от x
def input(x):
    return -np.sqrt(25 - x**2)  # Вычисление верхней границы по y, которая зависит от x

# Функция для интегрирования по x
def integrand(y, x):
    if y**2 + x**2 <= 25:
        return f(x, y)
    return 0

result, error = dblquad(integrand, -5, 5, lambda x: input(x), lambda x: output(x))

print("Результат интеграла:", result)