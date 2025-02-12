import numpy as np
import sympy as sp
# ------------------ Riemann midpoint method ------------------

def Composite_Simpson_rule(f, a, b, N, h):
    integral = 0

    for i in range(1, int(N / 2) - 1):
        x = a + 2 * i * h
        integral += 2 * f(x)


    for i in range(1, int(N / 2)):
        x = a + (2 * i - 1) * h
        integral += 4 * f(x)

    integral += f(a) + f(b)

    return (h / 3) * (integral)

# ------------------ Task 2 ------------------

eps = 0.001

f = lambda x: sp.sin(x) / (2 + sp.sin(x)) 

a = 0
b = sp.pi / 2

n = 10

N = 2 * n

h = (b - a) / N

alg_presicion = 3

print("n = " + str(n))

fi_h = Composite_Simpson_rule(f, a, b, N, h)
fi_2h = Composite_Simpson_rule(f, a, b, N/2, 2*h)

E = abs(fi_h - fi_2h) / (2**(alg_presicion) - 1)
while E >= eps:
    h = h / 2
    n = sp.floor((b - a) / h)
    fi_h = Composite_Simpson_rule(f, a, b, n, h)
    fi_2h = Composite_Simpson_rule(f, a, b, n/2, 2 * h)
    E = abs(fi_h - fi_2h) / (2**(alg_presicion) - 1)
    print(E.evalf())

print("Composite_Simpson_rule(h):", round(fi_h.evalf(), 4))
print("Composite_Simpson_rule(2h):", round(fi_2h.evalf(), 4))

x = sp.symbols('x')
exact_result = sp.integrate(f(x), (x, a, b))
print("Referense(sympy):", exact_result.evalf())