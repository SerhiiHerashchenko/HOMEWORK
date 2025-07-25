import numpy as np
import matplotlib.pyplot as plt

r = 5

theta = np.linspace(0, 2 * np.pi, 1000)
x_circle = r * np.cos(theta)
y_circle = r * np.sin(theta)

square_x = np.array([-r / np.sqrt(2), r / np.sqrt(2), r / np.sqrt(2), -r / np.sqrt(2), -r / np.sqrt(2)])
square_y = np.array([-r / np.sqrt(2), -r / np.sqrt(2), r / np.sqrt(2), r / np.sqrt(2), -r / np.sqrt(2)])

fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(x_circle, y_circle, 'b', label='circle', linewidth=2)
ax.plot(square_x, square_y, 'r-', label='square', linewidth=2)

ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='best')

ax.set_xlim(-r - 1, r + 1)
ax.set_ylim(-r - 1, r + 1)

plt.savefig('C:\All\Programs\GitHub repositories\HOMEWORK\Python\\1_SEMESTER\L3_V2_Herashchenko\8_task\circle_square.png', dpi=400)

plt.show()