import sympy as sp

# ------------------ Legendre polinomial ------------------
def legendre_poly(n, x):

    P_0 = 1
    P_1 = x
    
    if n == 0:
        return P_0
    elif n == 1:
        return P_1
    
    P_prev2 = P_0
    P_prev1 = P_1
    
    for i in range(2, int(n + 1)):
        P_current = ((2 * i - 1) * x * P_prev1 - (i - 1) * P_prev2) / i
        P_prev2 = P_prev1
        P_prev1 = P_current
    
    return P_current

# def gauss_quadrature(f, a, b, n):
#     x = sp.symbols('x')
    
#     legendre_poly_expr = legendre_poly(n, x)
    
#     roots = sp.solvers.solve(legendre_poly_expr, x)
#     roots = [float(root) for root in roots]
    
#     weights = []
#     roots_transformed = []
#     for root in roots:
#         weight = 2 / ((1 - root**2) * (sp.diff(legendre_poly_expr, x).subs(x, root))**2)
#         weights.append(float(weight))
#         roots_transformed.append(0.5 * (root) * (b - a) + (b + a) * 0.5)

#     integral = 0
#     for i in range(int(n)):
#         integral += weights[i] * f(roots_transformed[i])

#     return ((b - a) / 2) * integral

# ------------------ Gauss quadrature formula ------------------

def gauss_quadrature(f, a, b, n):
    roots = []
    weights = []

    if n == 5:
        roots = [-0.906179845938664, -0.538469310105683, 0, 0.538469310105683, 0.906179845938664]
        weights = [0.236926885056189, 0.478628670499366, 0.568888888888889, 0.478628670499366, 0.236926885056189]
    elif n == 4:
        roots = [-0.861136311594053, -0.339981043584856, 0.339981043584856, 0.861136311594053]
        weights = [0.3478548451374529, 0.6521451548625463, 0.6521451548625463, 0.3478548451374529]
    elif n == 3:
        roots = [-0.774596669241483, 0, 0.774596669241483]
        weights = [0.555555555555556, 0.888888888888889, 0.555555555555556]
    elif n == 2:
        roots = [-0.577350269189626, 0.577350269189626]
        weights = [1, 1]
    elif n == 1:
        roots = [0]
        weights = [2]


    roots_transformed = []
    for root in roots:
        roots_transformed.append(0.5 * (root) * (b - a) + (b + a) * 0.5)

    integral = 0
    for i in range(int(n)):
        integral += weights[i] * f(roots_transformed[i])

    return ((b - a) / 2) * integral

# ------------------ My Integral ------------------

eps = 0.001

f = lambda x: sp.sin(x) / (2 + sp.sin(x)) 

a = 0
b = sp.pi / 2

n = 2

h = (b - a) / n

alg_presicion = 2 * n - 1

result_h = gauss_quadrature(f, a, b, n)
result_2h = gauss_quadrature(f, a, b, n/2)
print("n = " + str(n))

E = abs(result_h - result_2h) / (2**(alg_presicion) - 1)
print("Error:", E.evalf())

# ------------------ Runge Accuracy Control ------------------
while E >= eps:
    h = h / 2
    n = 2 * n
    result_h = gauss_quadrature(f, a, b, n)
    result_2h = gauss_quadrature(f, a, b, n/2)
    E = abs(result_h - result_2h) / (2**(alg_presicion) - 1)
    print("n = " + str(n))
    print("Error:", E.evalf())

print("Gauss quadrature formula(h):", round(result_h.evalf(), 4))

x = sp.symbols('x')
exact_result = sp.integrate(f(x), (x, a, b))
print("Referense(sympy):", exact_result.evalf())