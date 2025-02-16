import sympy as sp
# ------------------ Composite Simpson rule ------------------

def Composite_Simpson_rule(f, a, b, n, h):
    integral = 0

    for i in range(1, int(n)):
        x = a + 2 * i * h
        integral += 2 * f(x)

    for i in range(1, int(n) + 1):
        x = a + (2 * i - 1) * h
        integral += 4 * f(x)

    integral += f(a) + f(b)

    return (h / 3) * (integral)

# ------------------ My Integral ------------------

eps = 0.001

f = lambda x: sp.sin(x) / (2 + sp.sin(x)) 

a = 0
b = sp.pi / 2

n = 3
N = 2 * n

h = (b - a) / N

alg_presicion = 3

print("n = " + str(n))

result_h = Composite_Simpson_rule(f, a, b, n, h)
result_2h = Composite_Simpson_rule(f, a, b, n/2, 2*h)

E = abs(result_h - result_2h) / (2**(alg_presicion) - 1)
print("Error:", E.evalf())

# ------------------ Runge Accuracy Control ------------------
while E >= eps:
    n *= 2
    N = 2 * n
    h = (b - a) / N
    result_h = Composite_Simpson_rule(f, a, b, n, h)
    result_2h = Composite_Simpson_rule(f, a, b, n / 2, h * 2)
    E = abs(result_h - result_2h) / (2**(alg_presicion) - 1)
    print("n = " + str(n))
    print("Error:", E.evalf())

print("Composite Simpson rule(h):", round(result_h.evalf(), 4))

x = sp.symbols('x')
exact_result = sp.integrate(f(x), (x, a, b))
print("Referense(sympy):", exact_result.evalf())