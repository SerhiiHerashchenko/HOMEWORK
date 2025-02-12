import sympy as sp

x, y = sp.symbols('x y')

f = x**3 - y**2

grad_f = [sp.diff(f, var) for var in (x, y)]
grad_at_M = [grad.subs({x: 1, y: 1}) for grad in grad_f]
a = sp.Matrix([-3, 2])

a_norm = a.norm()
a_unit = a / a_norm

grad_at_M_matrix = sp.Matrix(grad_at_M)
directional_derivative = grad_at_M_matrix.dot(a_unit)

if directional_derivative > 0:
    direction = 'inc'
elif directional_derivative < 0:
    direction = 'dec'
else:
    direction = 'constant'

print(f"grad(f) in M(1, 1): {grad_at_M}")
print(f"derivative of f in M in a direction: {directional_derivative}")
print(f"Function f in M in a direction {'inc' if direction == 'inc' else 'dec' if direction == 'dec' else 'constant'}")