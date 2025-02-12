import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 2 * np.pi, 100)
y = np.linspace(1, 10, 100)
X, Y = np.meshgrid(x, y)

Z = np.sin(X) ** 2 * np.log(Y)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')
ax1.plot_wireframe(X, Y, Z, color='b', linewidth=0.5)
ax1.set_title('Wireframe')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
surf = ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.contour(X, Y, Z, zdir='z', offset=Z.min(), cmap='viridis')
fig2.colorbar(surf, shrink=0.5, aspect=10)
ax2.set_title('Surface plot')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

fig3 = plt.figure(figsize=(12, 6))

ax3_1 = fig3.add_subplot(131, projection='3d')
ax3_1.plot_surface(X, Y, Z, cmap='viridis')
ax3_1.view_init(30, 30)
ax3_1.set_title('Вид 1')

ax3_2 = fig3.add_subplot(132, projection='3d')
ax3_2.plot_surface(X, Y, Z, cmap='viridis')
ax3_2.view_init(60, 60)
ax3_2.set_title('Вид 2')

ax3_3 = fig3.add_subplot(133, projection='3d')
ax3_3.plot_surface(X, Y, Z, cmap='viridis')
ax3_3.view_init(120, 90)
ax3_3.set_title('Вид 3')

plt.show()