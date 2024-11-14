import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u, v = sp.symbols('u v')

x1 = sp.sin(u) * (1 - 0.2 * v)
y1 = 0.2 * sp.sin(u) * sp.cos(v)
z1 = sp.cos(u) * (1 + 0.2 * v)

x2 = 0.4 + (0.3 + sp.cos(v)) * sp.cos(u)
y2 = 0.4 + sp.sin(v)
z2 = 0.4 + (0.3 + sp.cos(v)) * sp.sin(u)

f_x1 = sp.lambdify((u, v), x1)
f_y1 = sp.lambdify((u, v), y1)
f_z1 = sp.lambdify((u, v), z1)

f_x2 = sp.lambdify((u, v), x2)
f_y2 = sp.lambdify((u, v), y2)
f_z2 = sp.lambdify((u, v), z2)

u_vals, v_vals = np.meshgrid(np.linspace(-5, 5, 400), np.linspace(-5, 5, 400))

x1_vals = f_x1(u_vals, v_vals)
y1_vals = f_y1(u_vals, v_vals)
z1_vals = f_z1(u_vals, v_vals)

u_vals2, v_vals2 = np.meshgrid(np.linspace(0, 2 * np.pi, 400), np.linspace(0, 2 * np.pi, 400))

x2_vals = f_x2(u_vals2, v_vals2)
y2_vals = f_y2(u_vals2, v_vals2)
z2_vals = f_z2(u_vals2, v_vals2)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x1_vals, y1_vals, z1_vals, color='b', alpha=0.5)

ax.plot_surface(x2_vals, y2_vals, z2_vals, color='r', alpha=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()