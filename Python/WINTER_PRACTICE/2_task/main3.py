import sympy as sp

# ------------------ Trapezoidal rule ------------------

def Trapezoidal_rule(f, a, b, n):

    h = (b - a) / n
    integral = 0

    for i in range(1, int(n)):
        x = a + i * h
        integral += f(x)

    integral += (f(a) + f(b)) / 2

    return h * integral

# ------------------ My Integral ------------------

eps = 0.001

f = lambda x: sp.sin(x) / (2 + sp.sin(x)) 

a = 0
b = sp.pi / 2

n = 10

h = (b - a) / n

alg_presicion = 1

print("n = " + str(n))

result_n = Trapezoidal_rule(f, a, b, n)
result_2n = Trapezoidal_rule(f, a, b, 2 * n)

E = abs(result_n - result_2n) / (2**(alg_presicion) - 1)
print("Error:", E.evalf())

# ------------------ Runge Accuracy Control ------------------

while E >= eps:
    n = 2 * n
    result_n = result_2n
    result_2n = Trapezoidal_rule(f, a, b, 2 * n)
    E = abs(result_n - result_2n) / (2**(alg_presicion) - 1)
    print("n = " + str(n))
    print("Error:", E.evalf())

print("Riemann midpoint method(h):", round(result_n.evalf(), 4))

x = sp.symbols('x')
exact_result = sp.integrate(f(x), (x, a, b))
print("Referense(sympy):", exact_result.evalf())