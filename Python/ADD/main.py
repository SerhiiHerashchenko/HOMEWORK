class LongFloat:
    def __init__(self, *args):
        """
        Конструктор класса LongFloat.
        Принимает либо число с плавающей точкой (float), либо мантиссу (целое число), порядок и знак.
        """
        if len(args) == 1 and isinstance(args[0], float):
            # Конструктор для числа с плавающей точкой
            self._sign = -1 if args[0] < 0 else 1
            abs_value = abs(args[0])
            self._mantissa, self._exponent = self._float_to_mantissa_exponent(abs_value)
        elif len(args) == 3:
            # Конструктор для мантиссы, порядка и знака
            self._mantissa, self._exponent, self._sign = args
        else:
            raise ValueError("Неправильное количество аргументов")

    def _float_to_mantissa_exponent(self, value):
        """Преобразует число с плавающей точкой в мантиссу и показатель степени"""
        exponent = 0
        while value >= 10:
            value /= 10
            exponent += 1
        while value < 1:
            value *= 10
            exponent -= 1
        mantissa = int(value * 10**9)  # Делаем мантиссу целым числом с точностью до 9 знаков
        return mantissa, exponent

    def __str__(self):
        """Возвращает строковое представление числа в формате <знак>0.<мантисса>E<степень>"""
        return f"{'-' if self._sign == -1 else ''}0.{str(self._mantissa).zfill(9)}E{self._exponent:+03d}"

    # Сравнение
    def __lt__(self, other):
        return self._compare(other) < 0

    def __le__(self, other):
        return self._compare(other) <= 0

    def __eq__(self, other):
        return self._compare(other) == 0

    def _compare(self, other):
        """Сравнение двух объектов LongFloat"""
        if not isinstance(other, LongFloat):
            raise ValueError("Сравнение возможно только с объектом LongFloat")
        
        # Сравниваем мантиссу и показатель степени
        if self._exponent != other._exponent:
            return self._exponent - other._exponent
        return self._mantissa - other._mantissa

    # Арифметическая операция сложения
    def __add__(self, other):
        if not isinstance(other, LongFloat):
            raise ValueError("Сложение возможно только с объектом LongFloat")
        
        # Приводим к одинаковому порядку степеней
        if self._exponent > other._exponent:
            mantissa_self = self._mantissa
            mantissa_other = other._mantissa * (10 ** (self._exponent - other._exponent))
            exponent = self._exponent
        else:
            mantissa_self = self._mantissa * (10 ** (other._exponent - self._exponent))
            mantissa_other = other._mantissa
            exponent = other._exponent

        # Сложение мантисс с учетом знаков
        mantissa_result = mantissa_self + mantissa_other
        sign = 1 if mantissa_result >= 0 else -1
        mantissa_result = abs(mantissa_result)

        # Нормализация
        while mantissa_result >= 10**9:
            mantissa_result //= 10
            exponent += 1
        while mantissa_result < 10**8:
            mantissa_result *= 10
            exponent -= 1

        return LongFloat(mantissa_result * sign, exponent, sign)


# Пример использования
if __name__ == "__main__":
    # Пример чисел с плавающей точкой
    num1 = LongFloat(-0.864197532E+10)
    num2 = LongFloat(4.5)

    # Строковое представление
    print("Число 1:", num1)
    print("Число 2:", num2)

    # Сравнение чисел
    print("num1 < num2:", num1 < num2)
    print("num1 <= num2:", num1 <= num2)
    print("num1 == num2:", num1 == num2)

    # Сложение чисел
    sum_result = num1 + num2
    print("Сумма чисел:", sum_result)
