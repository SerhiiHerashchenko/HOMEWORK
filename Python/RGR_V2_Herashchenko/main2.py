import numpy as np

# 1. Кубатурная формула
def double_integral_cubature(n):
    """
    Вычисление двойного интеграла по кубатурной формуле для области x^4 + y^4 <= 1
    """
    def f(x, y):
        return x**2 + y**2  # Новая функция интеграла

    R = 1  # Радиус области (ограничение по x^4 + y^4 <= 1)

    # Узлы (x, y) и веса w для квадратуры Гаусса
    points, weights = np.polynomial.legendre.leggauss(n)  # Узлы и веса на интервале [-1, 1]
    
    # Масштабируем узлы и веса для области x^4 + y^4 <= 1
    points_x = points  # Узлы на интервале [-1, 1]
    weights_x = weights  # Веса для квадратуры
    points_y = points_x  # Используем те же узлы для y, так как область симметрична
    weights_y = weights_x

    # Считаем интеграл как сумму по узлам
    integral = 0
    for i, y in enumerate(points_y):
        for j, x in enumerate(points_x):
            # Проверяем, чтобы точка находилась внутри области x^4 + y^4 <= 1
            if x**4 + y**4 <= 1:
                integral += weights_x[j] * weights_y[i] * f(x, y)
    
    return integral


# 2. Метод Симпсона
def double_integral_simpson(n):
    """
    Вычисление двойного интеграла методом Симпсона для области x^4 + y^4 <= 1
    """
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


# Основная функция для вычисления обоих интегралов
def calculate_integrals(n):
    """
    Вычисление двойных интегралов с использованием кубатурной формулы и метода Симпсона
    """
    cubature_result = double_integral_cubature(n)  # Кубатурная формула
    simpson_result = double_integral_simpson(n)  # Метод Симпсона
    
    return cubature_result, simpson_result


# Проверка функции для различных n
n = 2000  # Количество разбиений для лучшего результата
cubature_result, simpson_result = calculate_integrals(n)

print("Результат кубатурной формулы:", cubature_result)
print("Результат метода Симпсона:", simpson_result)
