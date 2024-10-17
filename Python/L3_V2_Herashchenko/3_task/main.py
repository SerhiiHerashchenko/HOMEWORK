import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 1, 100)
y1 = np.sqrt(x1)

x2 = np.linspace(1.01, 3, 100)
y2 = np.ones_like(x2)

x3 = np.linspace(3.01, 5, 100)
y3 = (x3 - 4) ** 2

plt.figure(figsize=(8, 6))

plt.plot(x1, y1, label=r'$\sqrt{x}$ on [0, 1]', color='b', linestyle='-', linewidth=2)

plt.plot(x2, y2, label=r'$1$ on (1, 3]', color='g', linestyle='--', linewidth=2)

plt.plot(x3, y3, label=r'$(x - 4)^2$ on (3, 5]', color='r', linestyle='-.', linewidth=2)

plt.title('f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

plt.show()
