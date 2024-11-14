import sympy as sp

x, y = sp.symbols('x y')

f = sp.cos(x + y) * sp.exp(x * y)

f_x = sp.diff(f, x)
f_y = sp.diff(f, y)

f_xx = sp.diff(f_x, x)
f_yy = sp.diff(f_y, y)
f_xy = sp.diff(f_x, y)
f_yx = sp.diff(f_y, x)

f_x = sp.simplify(f_x)
f_y = sp.simplify(f_y)
f_xx = sp.simplify(f_xx)
f_yy = sp.simplify(f_yy)
f_xy = sp.simplify(f_xy)
f_yx = sp.simplify(f_yx)

print(f"x: {f_x}")
print(f"y: {f_y}")
print(f"xx: {f_xx}")
print(f"yy: {f_yy}")
print(f"xy: {f_xy}")
print(f"yx: {f_yx}")
