import sympy as sp

# ------------------ Gauss quadrature formula ------------------

def gauss_quadrature(f, a, b, n, alg_presicion):
    roots = []
    weights = []

    if alg_presicion == 5:
        roots = [-0.906179845938664, -0.538469310105683, 0, 0.538469310105683, 0.906179845938664]
        weights = [0.236926885056189, 0.478628670499366, 0.568888888888889, 0.478628670499366, 0.236926885056189]
    elif alg_presicion == 4:
        roots = [-0.861136311594053, -0.339981043584856, 0.339981043584856, 0.861136311594053]
        weights = [0.3478548451374529, 0.6521451548625463, 0.6521451548625463, 0.3478548451374529]
    elif alg_presicion == 3:
        roots = [-0.774596669241483, 0, 0.774596669241483]
        weights = [0.555555555555556, 0.888888888888889, 0.555555555555556]
    elif alg_presicion == 2:
        roots = [-0.577350269189626, 0.577350269189626]
        weights = [1, 1]
    elif alg_presicion == 1:
        roots = [0]
        weights = [2]

    h = (b - a) / n
    integral = 0
    for i in range(int(n)):
        tmp_a = a + i * h
        tmp_b = tmp_a + h
        tmp_integral = 0
        for j in range(alg_presicion):
            root_mapped = 0.5 * (roots[j]) * (tmp_b - tmp_a) + (tmp_b + tmp_a) * 0.5
            tmp_integral += weights[j] * f(root_mapped)
        integral += ((tmp_b - tmp_a) / 2) * tmp_integral


    return integral

# ------------------ My Integral ------------------

eps = 0.001

f = lambda x: sp.sin(x) / (2 + sp.sin(x)) 

a = 0
b = sp.pi / 2

n = 2

h = (b - a) / n

alg_presicion = 2 * n - 1

result_n = gauss_quadrature(f, a, b, n, alg_presicion)
result_2n = gauss_quadrature(f, a, b, 2 * n, alg_presicion)
print("n = " + str(n))

E = abs(result_n - result_2n) / (2**(alg_presicion) - 1)
print("Error:", E.evalf())

# ------------------ Runge Accuracy Control ------------------

while E >= eps:
    h = h / 2
    n = 2 * n
    result_n = result_2n
    result_2n = gauss_quadrature(f, a, b, 2 * n, alg_presicion)
    E = abs(result_n - result_2n) / (2**(alg_presicion) - 1)
    print("n = " + str(n))
    print("Error:", E.evalf())

print("Gauss quadrature formula(h):", round(result_n.evalf(), 4))

x = sp.symbols('x')
exact_result = sp.integrate(f(x), (x, a, b))
print("Referense(sympy):", exact_result.evalf())