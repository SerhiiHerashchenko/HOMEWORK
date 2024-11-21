import numpy as np
from scipy.integrate import dblquad

def double_integral_cubature_simpson(n):
    """
    Вычисление двойного интеграла методом кубатурной формулы Симпсона с улучшенной точностью.
    """
    def f(x, y):
        return x**2 + y**2  # Функция под интегралом
    
    a, A = -1, 1  # Границы интегрирования по x
    b, B = -1, 1  # Границы интегрирования по y

    # Шаги разбиения
    h = (A - a) / (2 * n)  # Шаг по x
    k = (B - b) / (2 * n)  # Шаг по y
    
    integral = 0
    
    # Разбиваем область на прямоугольники и применяем формулу
    for i in range(n):
        for j in range(n):
            # Границы текущего прямоугольника
            x0, x2 = a + 2 * i * h, a + 2 * i * h + 2 * h
            x1 = x0 + h
            y0, y2 = b + 2 * j * k, b + 2 * j * k + 2 * k
            y1 = y0 + k
            
            # Проверка всех точек (x0, y0), (x1, y0), (x0, y1), (x2, y0), (x2, y1), (x1, y2), (x0, y2), (x2, y2) на попадание в область
            points = [(x0, y0), (x1, y0), (x0, y1), (x2, y0), (x2, y1), (x1, y2), (x0, y2), (x2, y2)]
            if any(x**4 + y**4 > 1 for x, y in points):  # Если хотя бы одна точка выходит за границу, пропускаем этот прямоугольник
                continue
            
            # Формула Симпсона на прямоугольнике
            local_integral = (h * k / 9) * (
                f(x0, y0) + f(x2, y0) + f(x0, y2) + f(x2, y2) +
                4 * (f(x1, y0) + f(x0, y1) + f(x2, y1) + f(x1, y2)) +
                16 * f(x1, y1)
            )
            
            # Добавляем вклад от прямоугольника
            integral += local_integral
    
    return integral

# 2. Метод Симпсона
def double_integral_simpson(n):
    N = 2 * n  # Количество разбиений для более точного результата

    def f(x, y):
        return x**2 + y**2  # Новая функция интеграла

    R = 1  # Радиус области (ограничение по x^4 + y^4 <= 1)

    # Внешний интеграл
    def simpson_outer(y):
        a, b = -np.sqrt(1 - y**4), np.sqrt(1 - y**4)  # Границы по x для данной y
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

print("Результат кубатурной формулы:", double_integral_cubature_simpson(n=200))
print("Результат метода Симпсона:", double_integral_simpson(n=200))

# ---------------- Референсное значение ----------------

def f(x, y):
    return x**2 + y**2 # Функция под интегралом
def output(x):
    return np.sqrt(1 - x**4)  # Вычисление верхней границы по y, которая зависит от x
def input(x):
    return -np.sqrt(1 - x**4)  # Вычисление верхней границы по y, которая зависит от x

# Функция для интегрирования по x
def integrand(y, x):
    if y**4 + x**4 <= 1:
        return f(x, y)
    return 0

result, error = dblquad(integrand, -1, 1, lambda x: input(x), lambda x: output(x))

print("Результат интеграла:", result)