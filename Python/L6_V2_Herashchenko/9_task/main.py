import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt

# Данные
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([5, -1, 3, 2, 0, 8])

# 1. Интерполяционный многочлен Лагранжа
lagrange_interpolator = interp.lagrange(x_data, y_data)

# 2. Интерполяционный сплайн 1-й степени (линейный)
linear_spline = interp.PchipInterpolator(x_data, y_data)

# 3. Интерполяционный сплайн 3-й степени (кубический)
cubic_spline = interp.CubicSpline(x_data, y_data)

# Точки для построения графиков
x_vals = np.linspace(0, 5, 400)

# Значения интерполяции для каждой функции
y_lagrange = lagrange_interpolator(x_vals)
y_linear = linear_spline(x_vals)
y_cubic = cubic_spline(x_vals)

# Построение графиков
plt.figure(figsize=(10, 6))

# График интерполяции Лагранжа
plt.plot(x_vals, y_lagrange, label='Многочлен Лагранжа', color='blue', linestyle='-')

# График линейного сплайна
plt.plot(x_vals, y_linear, label='Линейный сплайн', color='green', linestyle='--')

# График кубического сплайна
plt.plot(x_vals, y_cubic, label='Кубический сплайн', color='red', linestyle='-.')

# Исходные данные
plt.scatter(x_data, y_data, color='black', zorder=5, label='Табличные точки')

# Настройка графика
plt.title('Интерполяционные многочлены и сплайны')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
