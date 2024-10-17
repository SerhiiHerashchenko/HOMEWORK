import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0, 8 * np.pi, 100)
rho = 2 * phi

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')

ax.plot(phi, rho, color='green', marker='*', linewidth=1)

ax.set_title(r'$\rho = 2\varphi$', va='bottom')

plt.show()
