import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Определение функций для уравнений и неравенств
def line1(x1):
    return 14 - 5 * x1

def line2(x1):
    return 13 - 2 * x1

def line3(x1):
    return 13 - x1

# Находим точки пересечения с помощью fsolve
def intersection(func1, func2):
    return fsolve(lambda x: func1(x) - func2(x), 0)[0]

# Точки пересечения линий
x1_A = intersection(line1, line2)
A = (x1_A, line1(x1_A))

x1_B = intersection(line2, line3)
B = (x1_B, line2(x1_B))

x1_C = intersection(line1, line3)
C = (x1_C, line1(x1_C))

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(8, 8))

# Определяем диапазон для x1, приближая график к точкам пересечения
x1_vals = np.linspace(0, 17, 400)

# Строим графики функций, ограничивая область значений y
y1_vals = line1(x1_vals)
y2_vals = line2(x1_vals)
y3_vals = line3(x1_vals)

# Строим графики функций
ax.plot(x1_vals, y1_vals, label=r'$5x_1 + x_2 = 14$', color='b')
ax.plot(x1_vals, y2_vals, label=r'$2x_1 + x_2 \geq 13$', color='g')
ax.plot(x1_vals, y3_vals, label=r'$x_1 + x_2 \leq 13$', color='r')

# Заполняем области для неравенств
x1_fill = np.linspace(0, 16, 200)
ax.fill_between(x1_fill, line2(x1_fill), 16, where=(line2(x1_fill) < 16), color='lightgreen', alpha=0.5)
ax.fill_between(x1_fill, line3(x1_fill), 0, where=(line3(x1_fill) >= 0), color='lightcoral', alpha=0.5)

# Обозначаем точки пересечения буквами
ax.plot(*A, 'ko')
ax.text(A[0], A[1], 'A', fontsize=12, ha='right', va='top')

ax.plot(*B, 'ko')
ax.text(B[0], B[1], 'B', fontsize=12, ha='right', va='top')

ax.plot(*C, 'ko')
ax.text(C[0], C[1], 'C', fontsize=12, ha='left', va='bottom')

# Выделяем отрезок AC жирным черным цветом
ax.plot([A[0], C[0]], [A[1], C[1]], 'k-', linewidth=3)

# Настройка ограничений на оси и отображение
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 15)

# Убираем сетку и выделяем оси координат
ax.axhline(0, color='black', lw=1.5)
ax.axvline(0, color='black', lw=1.5)

# Отображаем легенду
ax.legend()

# Отображаем график
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('Графiки функцiй обмежень')
plt.show()
