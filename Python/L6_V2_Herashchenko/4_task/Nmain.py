import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Задаем уравнение y''' + 3y'' + 8y - 2 = 0 в виде системы первого порядка
def ode_system(t, y):
    # y[0] = y, y[1] = y', y[2] = y''
    dydt = [y[1],  # y' = y[1]
            y[2],  # y'' = y[2]
            -3*y[2] - 8*y[0] + 2]  # y''' = -3y'' - 8y + 2
    return dydt

# Начальные условия
y0 = [3, -2, 5]  # y(0), y'(0), y''(0)

# Решаем задачу Коши на интервале [0, 10]
t_span = (0, 10)
t_eval = np.linspace(0, 10, 500)  # Точки, где вычисляем решение
solution = solve_ivp(ode_system, t_span, y0, t_eval=t_eval, method='RK45')

# Извлекаем результаты
t = solution.t
y = solution.y[0]  # y(x)
y_prime = solution.y[1]  # y'(x)
y_double_prime = solution.y[2]  # y''(x)

# Построение графиков
plt.figure(figsize=(10, 6))

# График y(x)
plt.plot(t, y, label="y(x)", color='blue')

# График y'(x)
plt.plot(t, y_prime, label="y'(x)", color='green')

# График y''(x)
plt.plot(t, y_double_prime, label="y''(x)", color='red')

# Настройки графиков
plt.title("Решение задачи Коши и производные")
plt.xlabel("x")
plt.ylabel("y, y', y''")
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend()
plt.grid()
plt.show()
