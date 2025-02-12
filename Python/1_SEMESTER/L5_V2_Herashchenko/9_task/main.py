import sympy as sp

x1, x2, x3, y1, y2, y3 = sp.symbols('x1 x2 x3 y1 y2 y3')

u = 1 / sp.sqrt((x1 - y1)**2 + (x2 - y2)**2 + (x3 - y3)**2)

u_x1 = sp.diff(u, x1, 2)
u_x2 = sp.diff(u, x2, 2)
u_x3 = sp.diff(u, x3, 2)

laplacian = u_x1 + u_x2 + u_x3

laplacian_simplified = sp.simplify(laplacian)

print(laplacian_simplified)
