import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определяем символы
u, v = sp.symbols('u v')

# Параметрическое уравнение для первой поверхности
x1 = sp.sin(u) * (1 - 0.2 * v)
y1 = 0.2 * sp.sin(u) * sp.cos(v)
z1 = sp.cos(u) * (1 + 0.2 * v)

# Параметрическое уравнение для второй поверхности
x2 = 0.4 + (0.3 + sp.cos(v)) * sp.cos(u)
y2 = 0.4 + sp.sin(v)
z2 = 0.4 + (0.3 + sp.cos(v)) * sp.sin(u)

# Создаем числовые функции для вычислений
f_x1 = sp.lambdify((u, v), x1, 'numpy')
f_y1 = sp.lambdify((u, v), y1, 'numpy')
f_z1 = sp.lambdify((u, v), z1, 'numpy')

f_x2 = sp.lambdify((u, v), x2, 'numpy')
f_y2 = sp.lambdify((u, v), y2, 'numpy')
f_z2 = sp.lambdify((u, v), z2, 'numpy')

# Создаем сетку для u и v
u_vals, v_vals = np.meshgrid(np.linspace(-5, 5, 400), np.linspace(-5, 5, 400))

# Вычисляем координаты для первой поверхности
x1_vals = f_x1(u_vals, v_vals)
y1_vals = f_y1(u_vals, v_vals)
z1_vals = f_z1(u_vals, v_vals)

# Создаем сетку для u и v для второй поверхности
u_vals2, v_vals2 = np.meshgrid(np.linspace(0, 2 * np.pi, 400), np.linspace(0, 2 * np.pi, 400))

# Вычисляем координаты для второй поверхности
x2_vals = f_x2(u_vals2, v_vals2)
y2_vals = f_y2(u_vals2, v_vals2)
z2_vals = f_z2(u_vals2, v_vals2)

# Создаем фигуру для графиков
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Строим первую поверхность
ax.plot_surface(x1_vals, y1_vals, z1_vals, color='b', alpha=0.5, label='Первая поверхность')

# Строим вторую поверхность
ax.plot_surface(x2_vals, y2_vals, z2_vals, color='r', alpha=0.5, label='Вторая поверхность')

# Настройки отображения
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Показываем график
plt.show()
