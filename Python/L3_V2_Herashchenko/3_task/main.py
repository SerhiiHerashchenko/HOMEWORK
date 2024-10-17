import numpy as np
import matplotlib.pyplot as plt

# Создание участков для кусочно-заданной функции
x1 = np.linspace(0, 1, 100)  # Участок [0, 1]
y1 = np.sqrt(x1)             # y = sqrt(x)

x2 = np.linspace(1.01, 3, 100)  # Участок (1, 3]
y2 = np.ones_like(x2)            # y = 1

x3 = np.linspace(3.01, 5, 100)  # Участок (3, 5]
y3 = (x3 - 4) ** 2              # y = (x - 4)^2

# Построение графика
plt.figure(figsize=(8, 6))

# Ветвь 1: sqrt(x)
plt.plot(x1, y1, label=r'$\sqrt{x}$ on [0, 1]', color='b', linestyle='-', linewidth=2)

# Ветвь 2: y = 1
plt.plot(x2, y2, label=r'$1$ on (1, 3]', color='g', linestyle='--', linewidth=2)

# Ветвь 3: (x - 4)^2
plt.plot(x3, y3, label=r'$(x - 4)^2$ on (3, 5]', color='r', linestyle='-.', linewidth=2)

# Настройка осей и легенды
plt.title('f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
