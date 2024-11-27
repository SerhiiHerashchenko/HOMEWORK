import numpy as np
import sympy as sp

def gauss_quadrature(f, a, b, n):
    """
    Вычисление интеграла функции f на интервале [a, b] методом Гаусса по n точкам.
    :param f: Функция для интегрирования (должна быть функцией от переменной x)
    :param a: Левая граница интервала
    :param b: Правая граница интервала
    :param n: Количество точек Гаусса
    :return: Приближённое значение интеграла
    """
    # Нормализуем интервал [a, b] к интервалу [-1, 1]
    xi, w = np.polynomial.legendre.leggauss(n)  # Получаем корни и веса для Гаусса
    xi = 0.5 * (xi + 1) * (b - a) + a  # Преобразование корней из [-1, 1] в [a, b]
    w = 0.5 * w * (b - a)  # Преобразование весов

    integral = sum(w[i] * f(xi[i]) for i in range(n))  # Суммируем по точкам Гаусса
    return integral

# Пример использования
if __name__ == "__main__":
    # Определим многочлен степени 2n-1 для проверки
    n = 3  # Например, 3 точки Гаусса
    degree = 2 * n - 1
    f = lambda x: x**degree + 5*x**(degree-1)-3*x**3  # Многочлен степени 2n-1, например, x^5

    # Вычисляем интеграл методом Гаусса
    a = 0
    b = 1
    gauss_result = gauss_quadrature(f, a, b, n)
    print("Результат интегрирования методом Гаусса:", gauss_result)

    # Проверка с использованием sympy для точного результата
    x = sp.symbols('x')
    exact_result = sp.integrate(x**degree + 5*x**(degree-1)-3*x**3, (x, a, b))
    print("Точный результат с помощью sympy:", exact_result)

    # Сравнение результатов
    print("Результаты совпадают?", np.isclose(gauss_result, float(exact_result)))
