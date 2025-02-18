import sympy as sp
# ------------------ Riemann midpoint method ------------------

def Trapezoidal_rule(f, a, b, n, h):

    x = a
    integral = 0

    for i in range(int(n)):
        integral += ((f(x) + f(x + h)) / 2) * h
        x += h

    return integral

# ------------------ My Integral ------------------

eps = 0.001

f = lambda x: sp.sin(x) / (2 + sp.sin(x)) 

a = 0
b = sp.pi / 2

n = 10

h = (b - a) / n

alg_presicion = 1

print("n = " + str(n))

result_h = Trapezoidal_rule(f, a, b, n, h)
result_2h = Trapezoidal_rule(f, a, b, 2 * n, h / 2)

E = abs(result_h - result_2h) / (2**(alg_presicion) - 1)
print("Error:", E.evalf())

# ------------------ Runge Accuracy Control ------------------
while E >= eps:
    h = h / 2
    n = 2 * n
    result_h = Trapezoidal_rule(f, a, b, n, h)
    result_2h = Trapezoidal_rule(f, a, b, 2 * n, h / 2)
    E = abs(result_h - result_2h) / (2**(alg_presicion) - 1)
    print("n = " + str(n))
    print("Error:", E.evalf())

print("Trapezoidal rule(h):", round(result_h.evalf(), 4))

x = sp.symbols('x')
exact_result = sp.integrate(f(x), (x, a, b))
print("Referense(sympy):", exact_result.evalf())