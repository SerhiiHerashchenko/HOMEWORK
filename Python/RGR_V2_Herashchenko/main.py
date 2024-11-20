import numpy as np

# 1. Кубатурная формула
def double_integral_quadrature(n=100):
    """
    Вычисление двойного интеграла по кубатурной формуле
    """
    R = 5  # радиус окружности
    integral = 0
    for i in range(n):
        for j in range(n):
            # Дискретизация
            x = -R + 2 * R * i / n
            y = -R + 2 * R * j / n
            if x**2 + y**2 <= R**2:  # проверка, что точка внутри круга
                f = 1 / np.sqrt(24 + x**2 + y**2)
                dA = (2 * R / n) ** 2  # площадь элемента
                integral += f * dA
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
print("Кубатурная формула:", double_integral_quadrature(n=200))
print("Метод Симпсона:", double_integral_simpson(n=200))
