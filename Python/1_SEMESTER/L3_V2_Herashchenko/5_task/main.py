import numpy as np
import matplotlib.pyplot as plt

A = np.array([[-5, 1], [-3, 1]])
b = np.array([3, -7])

solution = np.linalg.solve(A, b)
x_intersection, y_intersection = solution

x = np.linspace(-10, 10, 400)

def y1(x):
    return 5 * x + 3

def y2(x):
    return 3 * x - 7

plt.figure(figsize=(8, 6))

plt.plot(x, y1(x), label=r'$y_1 = 5x + 3$', color='b')
plt.plot(x, y2(x), label=r'$y_2 = 3x - 7$', color='g')

plt.plot(x_intersection, y_intersection, 'ro', markersize=8)
plt.text(x_intersection, y_intersection, 
         f'({int(x_intersection)}, {int(y_intersection)})', fontsize=12, ha='right', va='bottom')

plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True)
plt.legend(loc='best')

plt.show()