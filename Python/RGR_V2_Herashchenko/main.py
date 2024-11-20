import numpy as np

import numpy as np
from scipy.integrate import quad

def double_integral_cubature(n=5):
    R = 5  # Радиус окружности

    def f(x, y):
        return 1 / np.sqrt(24 + x**2 + y**2)

    # Узлы (x, y) и веса w для квадратуры Гаусса
    points, weights = np.polynomial.legendre.leggauss(n)  # Узлы и веса на интервале [-1, 1]
    
    # Преобразование узлов и весов для окружности радиуса R
    points_x = points * R  # Масштабируем узлы на диапазон [-R, R]
    weights_x = weights * R  # Масштабируем веса
    points_y = points_x  # Окружность симметрична по x и y
    weights_y = weights_x

    # Считаем интеграл как сумму по узлам
    integral = 0
    for i, y in enumerate(points_y):
        for j, x in enumerate(points_x):
            # Проверяем, чтобы точка находилась внутри круга
            if x**2 + y**2 <= R**2:
                integral += weights_x[j] * weights_y[i] * f(x, y)
    return integral


# 2. Метод Симпсона
def double_integral_simpson(n):
    
    N = 2 * n

    """
    Вычисление двойного интеграла методом Симпсона
    """
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
print("Кубатурная формула:", double_integral_cubature(n=200))
print("Метод Симпсона:", double_integral_simpson(n=200))
