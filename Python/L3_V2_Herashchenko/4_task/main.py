import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)

x = 2 * np.sin(t) - (2 / 3) * np.sin(2 * t)
y = 2 * np.cos(t) - (2 / 3) * np.cos(2 * t)

plt.figure(figsize=(6, 6))
plt.plot(x, y, label=r'$x(t)=2\sin(t)-\dfrac{2}{3}\sin(2t)$' + '\n' + r'$y(t)=2\cos(t)-\dfrac{2}{3}\cos(2t)$')

plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True)
plt.legend(loc='best')

plt.show()