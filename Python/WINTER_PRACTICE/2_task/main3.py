import numpy as np
import sympy as sp
# ------------------ Riemann midpoint method ------------------

def Trapezoidal_rule(f, a, b, n, h):

    x = a
    integral = 0

    for i in range(int(n)):
        integral += ((f(x) + f(x + h)) / 2) * h
        x += h

    return integral

# ------------------ Task 2 ------------------

eps = 0.001

f = lambda x: sp.sin(x) / (2 + sp.sin(x)) 

a = 0
b = sp.pi / 2

n = 10

h = (b - a) / n

alg_presicion = 1

print("n = " + str(n))

fi_h = Trapezoidal_rule(f, a, b, n, h)
fi_2h = Trapezoidal_rule(f, a, b, n/2, 2*h)

E = abs(fi_h - fi_2h) / (2**(alg_presicion) - 1)
while E >= eps:
    h = h / 2
    n = sp.floor((b - a) / h)
    fi_h = Trapezoidal_rule(f, a, b, n, h)
    fi_2h = Trapezoidal_rule(f, a, b, n/2, 2 * h)
    E = abs(fi_h - fi_2h) / (2**(alg_presicion) - 1)

print("Trapezoidal rule(h):", round(fi_h.evalf(), 4))
print("Trapezoidal rule(2h):", round(fi_2h.evalf(), 4))

x = sp.symbols('x')
exact_result = sp.integrate(f(x), (x, a, b))
print("Referense(sympy):", exact_result.evalf())