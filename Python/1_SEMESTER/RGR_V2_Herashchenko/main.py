import numpy as np
from scipy.integrate import dblquad
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return 1 / np.sqrt(24 + x**2 + y**2)

# ---------------- Кубатурый метод Симпсона ----------------

def double_integral_cubature_simpson(n):
    R = 5

    def f(x, y):
        return 1 / np.sqrt(24 + x**2 + y**2)

    a, A = -R, R
    b, B = -R, R

    h = (A - a) / (2 * n)
    k = (B - b) / (2 * n)

    integral = 0

    for i in range(n):
        for j in range(n):
            x0, x2 = a + 2 * i * h, a + 2 * i * h + 2 * h
            x1 = x0 + h
            y0, y2 = b + 2 * j * k, b + 2 * j * k + 2 * k
            y1 = y0 + k

            if x0**2 + y0**2 > R**2 or x2**2 + y2**2 > R**2:
                continue

            local_integral = (h * k / 9) * (
                f(x0, y0) + f(x2, y0) + f(x0, y2) + f(x2, y2) +
                4 * (f(x1, y0) + f(x0, y1) + f(x2, y1) + f(x1, y2)) +
                16 * f(x1, y1)
            )

            integral += local_integral

    return integral

# ---------------- Составной квадратурный метод Симпсона ----------------

def double_integral_simpson(n):
    
    N = 2 * n

    R = 5
    def f(x, y):
        return 1 / np.sqrt(24 + x**2 + y**2)
    
    def simpson_outer(y):
        a, b = -np.sqrt(R**2 - y**2), np.sqrt(R**2 - y**2)
        return simpson(lambda x: f(x, y), a, b, N)
    
    def simpson(func, a, b, N):
        h = (b - a) / N
        x = np.linspace(a, b, N + 1)
        s = func(x[0]) + func(x[-1])
        s += 4 * sum(func(x[1:N:2]))
        s += 2 * sum(func(x[2:N-1:2]))
        return s * h / 3
    
    integral = simpson(simpson_outer, -R, R, N)
    return integral

n=5000
print(f"n = {n}")
print("Кубатурная формула:", double_integral_cubature_simpson(n))
print("Метод Симпсона:", double_integral_simpson(n))

# ---------------- Референсное значение ----------------

def f(x, y):
    return 1 / np.sqrt(24 + x**2 + y**2)
def output(x):
    return np.sqrt(25 - x**2)
def input(x):
    return -np.sqrt(25 - x**2)
def integrand(y, x):
    if y**2 + x**2 <= 25:
        return f(x, y)
    return 0

result, error = dblquad(integrand, -5, 5, lambda x: input(x), lambda x: output(x))

print("Результат интеграла:", result)

# ---------------- График ----------------

R = 5

x = np.linspace(-R, R, 200)
y = np.linspace(-R, R, 200)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

mask = X**2 + Y**2 > R**2
Z[mask] = np.nan

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)

ax.set_title("Graph", fontsize=16)
ax.set_xlabel("X", fontsize=12)
ax.set_ylabel("Y", fontsize=12)
ax.set_zlabel("f(x, y)", fontsize=12)
plt.show()