from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import dblquad

f = lambda x, y: x**2 + y**2

def double_integral_cubature_simpson(n):
    a, A = -1, 1 
    b, B = -1, 1 

    # Шаги разбиения:
    h = (A - a) / (2 * n) 
    k = (B - b) / (2 * n) 
    
    integral = 0
    
    # Разбиваем область на прямоугольники
    for i in range(n):
        for j in range(n):
            # Границы текущего прямоугольника
            x0 = a + 2 * i * h
            x1 = x0 + h
            x2 = x1 + h
            
            y0 = b + 2 * j * k
            y1 = y0 + k
            y2 = y1 + k
            
            # Проверка всех точек на попадание в область
            points = [(x0, y0), (x0, y1), (x0, y2), (x1, y0), (x1, y1), (x1, y2), (x2, y0), (x2, y1), (x2, y2)]
            if any(x**4 + y**4 > 1 for x, y in points):
                continue
            
            # Формула Симпсона на прямоугольнике
            local_integral = (h * k / 9) * (
                f(x0, y0) + f(x2, y0) + f(x0, y2) + f(x2, y2) +
                4 * (f(x1, y0) + f(x0, y1) + f(x2, y1) + f(x1, y2)) +
                16 * f(x1, y1)
            )
            
            integral += local_integral
    
    return integral


def double_integral_simpson(n):
    R = 1  # Радиус области (ограничение по x^4 + y^4 <= 1)

    def simpson_inner(y):
        a, b = -np.power(1 - y**4, 1/4), np.power(1 - y**4, 1/4)
        return simpson(lambda x: f(x, y), a, b, n)

    def simpson(func, a, b, n): # Функция Симпсона для одномерного интеграла
        h = (b - a) / n  # Шаг разбиения
        x = np.linspace(a, b, 2 * n + 1)  # Узлы интегрирования
        s = func(x[0]) + func(x[-1])  # Первое и последнее значение
        s += 4 * sum(func(x[1:2*n:2]))  # Сумма по нечётным индексам
        s += 2 * sum(func(x[2:2*n-1:2]))  # Сумма по чётным индексам
        return s * h / 6

    integral = simpson(simpson_inner, -R, R, n)
    return integral

print("n = 200")
print("Результат кубатурної формули Сімпсона:", double_integral_cubature_simpson(n=200))
print("Результат складеної квадратурної формули Сімпсона:", double_integral_simpson(n=200))


output = lambda x: np.power(1 - x**4, 1/4)
input = lambda x: -np.power(1 - x**4, 1/4)
def integrand(y, x):
    if y**4 + x**4 <= 1:
        return f(x, y)
    return 0

result, error = dblquad(integrand, -1, 1, lambda x: input(x), lambda x: output(x))

print("Результат обчислення интегралу:", result)


x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

mask = X**4 + Y**4 > 1
Z[mask] = np.nan

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)

ax.set_title("Graph", fontsize=16)
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.set_zlabel("z", fontsize=12)
plt.show()