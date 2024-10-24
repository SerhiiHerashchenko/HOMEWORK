import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-np.pi, np.pi, 100)
x2 = np.linspace(-2, 2, 100)

f = np.sin(x1 ** 2)
g = np.cos(x1 ** 2)
u = x2 / 20
v = np.exp(x2)

plt.figure(figsize=(10, 5))
plt.plot(x1, f, label=r'$f(x) = \sin(x^2)$', color='b', linestyle='-', marker='o', markersize=4)
plt.plot(x1, g, label=r'$g(x) = \cos(x^2)$', color='r', linestyle='--', marker='x', markersize=4)
plt.title('$f(x)$ and $g(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)


plt.figure(figsize=(10, 5))
plt.plot(x2, u, label=r'$u(x) = \frac{x}{20}$', color='g', linestyle='-.', marker='s', markersize=4)
plt.plot(x2, v, label=r'$v(x) = e^x$', color='m', linestyle=':', marker='d', markersize=4)
plt.title('$u(x)$ and $v(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

ax1.plot(x1, f, label=r'$f(x) = \sin(x^2)$', color='b', linestyle='-', marker='o', markersize=4)
ax1.plot(x1, g, label=r'$g(x) = \cos(x^2)$', color='r', linestyle='--', marker='x', markersize=2)
ax1.set_title('$f(x)$ and $g(x)$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True)

ax2.plot(x2, u, label=r'$u(x) = \frac{x}{20}$', color='g', linestyle='-.', marker='s', markersize=4)
ax2.plot(x2, v, label=r'$v(x) = e^x$', color='m', linestyle=':', marker='d', markersize=3)
ax2.set_title('$u(x)$ and $v(x)$')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()