import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt

x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([5, -1, 3, 2, 0, 8])

lagrange_interpolator = interp.lagrange(x_data, y_data)

linear_spline = interp.PchipInterpolator(x_data, y_data)

cubic_spline = interp.CubicSpline(x_data, y_data)

x_vals = np.linspace(0, 5, 400)

y_lagrange = lagrange_interpolator(x_vals)
y_linear = linear_spline(x_vals)
y_cubic = cubic_spline(x_vals)

plt.figure(figsize=(10, 6))

plt.plot(x_vals, y_lagrange, label='Lagrange polynomial', color='blue', linestyle='-')

plt.plot(x_vals, y_linear, label='linear spline', color='green', linestyle='--')

plt.plot(x_vals, y_cubic, label='cubic spline', color='red', linestyle='-.')

plt.scatter(x_data, y_data, color='black', zorder=5, label='Given points')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

plt.show()
