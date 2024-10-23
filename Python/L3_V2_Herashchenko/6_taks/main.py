import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, np.abs(X))

left = (X**2 + Y**2 - 3) * R + np.sin(8 * R) * np.cos(6 * Theta)
right = (3 / 4) * (np.sin(5 * Theta) - 1)

Z = left - right

plt.figure(figsize=(9, 8))
plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar()
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True)

plt.show()