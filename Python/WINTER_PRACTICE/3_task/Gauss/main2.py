import numpy as np
import sympy as sp

# ------------------ Gauss Quadrature for Double Integrals ------------------

def Gauss_Quadrature_2d(f, a, A, b, B, n, alg_presicion):
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

    h_a = (A - a) / n
    h_b = (B - b) / n
    integral = 0

    for i in range(n):
        for j in range(n):
            a_tmp = a + i * h_a
            A_tmp = a_tmp + h_a
            b_tmp = b + j * h_b
            B_tmp = b_tmp + h_b

            integrel_tmp = 0
            for k in range(alg_presicion):
                x_transformed = ((A_tmp - a_tmp) / 2) * roots[k] + (A_tmp + a_tmp) / 2
                for l in range(alg_presicion):
                    y_transformed = ((B_tmp - b_tmp) / 2) * roots[l] + (B_tmp + b_tmp) / 2
                    integrel_tmp += (weights[k] * weights[l] * f(x_transformed, y_transformed))

            integral += ((A_tmp - a_tmp) / 2) * ((B_tmp - b_tmp) / 2) * integrel_tmp
    
    return integral

# ------------------ My Integral ------------------

eps = 0.001

f = lambda x, y: 2 * x * sp.sin(x * y)

a, A = 0, 1
b, B = 0, np.pi / 2

n = 2
alg_presicion = 2 * n - 1

print("n =", n)

result_n = Gauss_Quadrature_2d(f, a, A, b, B, n, alg_presicion)
result_2n = Gauss_Quadrature_2d(f, a, A, b, B, 2 * n, alg_presicion)

E = abs(result_n - result_2n) / (2**(alg_presicion) - 1)
print("Error:", E.evalf())

# ------------------ Runge Accuracy Control ------------------

while E >= eps:
    n = 2 * n
    result_n = result_2n
    result_2n = Gauss_Quadrature_2d(f, a, A, b, B, 2 * n, alg_presicion)
    E = abs(result_n - result_2n) / (2**(alg_presicion) - 1)
    print("n =", n)
    print("Error:", E.evalf())

print("Gauss quadrature formula(h):", round(result_n.evalf(), 4))

x, y = sp.symbols('x y')
exact_result = sp.integrate(f(x, y), (x, a, A), (y, b, B))
print("Reference(sympy):", exact_result.evalf())