import sympy as sp
# ------------------ Riemann midpoint method ------------------

def Riemann_midpoint_method(f, a, b, n):
    integral = 0
    h = (b - a) / n

    for i in range(int(n) + 1):
        x = a + (i - 0.5) * h
        integral += f(x)

    return h * integral

# ------------------ My Integral ------------------

eps = 0.001

f = lambda x: sp.sin(x) / (2 + sp.sin(x)) 

a = 0
b = sp.pi / 2

n = 10

alg_presicion = 1

print("n = " + str(n))

result_n = Riemann_midpoint_method(f, a, b, n)
result_2n = Riemann_midpoint_method(f, a, b, 2 * n)

E = abs(result_n - result_2n) / (2**(alg_presicion) - 1)
print("Error:", E.evalf())

# ------------------ Runge Accuracy Control ------------------
while E >= eps:
    n = 2 * n
    result_n = result_2n
    result_2n = Riemann_midpoint_method(f, a, b, 2 * n)
    E = abs(result_n - result_2n) / (2**(alg_presicion) - 1)
    print("n = " + str(n))
    print("Error:", E.evalf())

print("Riemann midpoint method(h):", round(result_n.evalf(), 4))

x = sp.symbols('x')
exact_result = sp.integrate(f(x), (x, a, b))
print("Referense(sympy):", exact_result.evalf())
