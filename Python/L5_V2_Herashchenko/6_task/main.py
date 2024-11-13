import sympy as sp

# Определяем переменные
x, y = sp.symbols('x y')

# Определяем функцию f(x, y)
f = x**3 - y**2

# 1. Вычисление градиента функции f в точке M(1, 1)
grad_f = [sp.diff(f, var) for var in (x, y)]  # Градиент функции f
grad_at_M = [grad.subs({x: 1, y: 1}) for grad in grad_f]  # Градиент в точке M(1, 1)

# 2. Направляющий вектор a=(-3, 2)
a = sp.Matrix([-3, 2])

# Нормализация вектора a
a_norm = a.norm()  # Вычисление длины вектора a
a_unit = a / a_norm  # Нормализованный вектор

# 3. Вычисление производной функции f в точке M по направлению нормализованного вектора
grad_at_M_matrix = sp.Matrix(grad_at_M)  # Градиент в виде матрицы
directional_derivative = grad_at_M_matrix.dot(a_unit)  # Производная по направлению нормализованного вектора

# 4. Определение возрастания или убывания функции в точке M по направлению
if directional_derivative > 0:
    direction = 'возрастает'
elif directional_derivative < 0:
    direction = 'убывает'
else:
    direction = 'не изменяется'

# Вывод результатов
print(f"Градиент функции f в точке M(1, 1): {grad_at_M}")
print(f"Производная функции f в точке M по направлению нормализованного вектора a: {directional_derivative}")
print(f"Функция f в точке M по направлению нормализованного вектора a {'возрастает' if direction == 'возрастает' else 'убывает' if direction == 'убывает' else 'не изменяется'}")
