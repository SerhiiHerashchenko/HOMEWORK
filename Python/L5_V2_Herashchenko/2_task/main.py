import sympy as sp

x = sp.symbols('x')

equation = sp.sin(x)**4 - sp.cos(x)**4 - 0.8

solutions = sp.solve(equation, x)

print("sin^4(x) - cos^4(x) - 0.8 = 0:")
for sol in solutions:
    print(sol)
