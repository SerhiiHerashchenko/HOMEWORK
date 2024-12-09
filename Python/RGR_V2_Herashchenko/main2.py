from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import dblquad

# ---------------- Кубатурый метод Симпсона ----------------

def f(x, y):
        return x**2 + y**2

def double_integral_cubature_simpson(n, f): # f - подынтегральная функция
    """
    Вычисление двойного интеграла методом кубатурной формулы Симпсона с улучшенной точностью.
    """
    
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
            x0 = a + 2 * i * h
            x1 = x0 + h
            x2 = x1 + h

            y0 = b + 2 * j * k
            y1 = y0 + k
            y2 = y1 + k
            
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

# ---------------- Составной квадратурный метод Симпсона ----------------

def double_integral_quadrature_simpson(n, f):  # f - подынтегральная функция
    R = 1  # Радиус области (ограничение по x^4 + y^4 <= 1)

    # Функция Симпсона для одномерного интеграла
    def simpson(func, a, b, n):
        h = (b - a) / n  # Шаг разбиения
        x = np.linspace(a, b, (2 * n) + 1)  # Узлы интегрирования
        s = func(x[0]) + func(x[-1])  # Первое и последнее значение
        s += 4 * sum(func(x[1:(2 * n):2]))  # Сумма по нечётным индексам
        s += 2 * sum(func(x[2:(2 * n)-1:2]))  # Сумма по чётным индексам
        return s * h / 6

    # Внутренний интеграл
    def simpson_inner(y):
        a, b = -np.power(1 - y**4, 1/4), np.power(1 - y**4, 1/4)  # Границы по x для данной y
        return simpson(lambda x: f(x, y), a, b, n)

    # Внешний интеграл
    integral = simpson(simpson_inner, -R, R, n)
    return integral

n = 1000
print(f"n = {n}")
print("Результат кубатурной формулы:", double_integral_cubature_simpson(n, f))
print("Результат метода Симпсона:", double_integral_quadrature_simpson(n, f))

# ---------------- Референсное значение ----------------

def f(x, y):
    return x**2 + y**2 # Функция под интегралом
def output(x):
    return np.power(1 - x**4, 1/4)  # Вычисление верхней границы по y, которая зависит от x
def input(x):
    return -np.power(1 - x**4, 1/4)  # Вычисление верхней границы по y, которая зависит от x

# Функция для интегрирования по x
def integrand(y, x):
    if y**4 + x**4 <= 1:
        return f(x, y)
    return 0

result, error = dblquad(integrand, -1, 1, lambda x: input(x), lambda x: output(x))

print("Результат интеграла:", result)

# ---------------- График ----------------

R = 1

x = np.linspace(-R, R, 200)
y = np.linspace(-R, R, 200)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

mask = X**4 + Y**4 > R**2
Z[X**4 + Y**4 > R**2] = np.nan

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)

ax.set_title("$x^2 + y^2$", fontsize=16)
ax.set_xlabel("X", fontsize=12)
ax.set_ylabel("Y", fontsize=12)
ax.set_zlabel("f(x, y)", fontsize=12)
plt.show()