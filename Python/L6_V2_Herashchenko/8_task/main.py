import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

def f(x):
    return (x - 5)**2 + (x - 2)**2

result1 = opt.minimize(f, x0=0)
print("scipy.optimize.minimize:", result1.x)

result2 = opt.fmin(f, x0=0) 
print("scipy.optimize.fmin:", result2)

def df(x):
    return 2 * (x - 5) + 2 * (x - 2)

result3 = opt.fminbound(f, -10, 10)
print("gradient descent(fminbound):", result3)

x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label=r'$f(x) = (x-5)^2 + (x-2)^2$')
plt.scatter(result1.x, f(result1.x), color='red', label=f'(minimize) at x = {result1.x[0]:.2f}')
plt.scatter(result2, f(result2), color='green', label=f'(fmin) at x = {result2[0]:.2f}')
plt.scatter(result3, f(result3), color='blue', label=f'(fminbound) at x = {result3:.2f}')
plt.title('Graph of the function f(x) and its minimums')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
