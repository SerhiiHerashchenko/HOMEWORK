import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import sympy as sp

# ======================================

x = sp.symbols('x')
C1, C2, C3 = sp.symbols('C1 C2 C3')
y = sp.Function('y')

eq = sp.Eq(y(x).diff(x, 3) + 3 * y(x).diff(x, 2) + 8 * y(x) - 2, 0)

general_solution = sp.dsolve(eq)
print(f"General solution:\n{general_solution} \n")

y_general = general_solution.rhs

ics = {
    y(0): 3,
    y(x).diff(x).subs(x, 0): -2,
    y(x).diff(x, 2).subs(x, 0): 5,
}

constants = sp.solve([y_general.subs(x, 0) - 3,
                      y_general.diff(x).subs(x, 0) + 2,
                      y_general.diff(x, 2).subs(x, 0) - 5], [C1, C2, C3])

specific_solution = y_general.subs(constants)
print(f"Specific solution:\ny(x) = {specific_solution}")

# ======================================

def ode_system(t, y):
    dydt = [y[1],
            y[2],
            -3*y[2] - 8*y[0] + 2]
    return dydt

y0 = [3, -2, 5]

t_span = (0, 10)
t = np.linspace(0, 10, 500)
solution = solve_ivp(ode_system, t_span, y0, t_eval=t, method='RK45')

y = solution.y[0]
y_prime = solution.y[1]
y_double_prime = solution.y[2]

# ======================================

plt.figure(figsize=(10, 6))

plt.plot(t, y, label="y(x)", color='blue')

plt.plot(t, y_prime, label="y'(x)", color='green')

plt.plot(t, y_double_prime, label="y''(x)", color='red')

plt.xlabel("x")
plt.ylabel("y, y', y''")
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend()
plt.grid()
plt.show()
