import numpy as np
import matplotlib.pyplot as plt

# Создаем данные для полярного графика
phi = np.linspace(0, 8 * np.pi, 100)  # Угол fi в интервале [0; 8pi]
rho = 2 * phi  # Функция rho = 2 * fi

# Построение полярного графика
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')  # Установка полярных координат

# График с зелёной линией, звёздными маркерами и толщиной линии 1
ax.plot(phi, rho, color='green', marker='*', linewidth=1)

# Настройка заголовка
ax.set_title(r'$\rho = 2\varphi$', va='bottom')

# Показать сетку и сам график

plt.show()
