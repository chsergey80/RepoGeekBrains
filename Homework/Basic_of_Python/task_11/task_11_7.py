"""
Задание 11.7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма c1 и c2 равна')
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение c1 и c2 равно')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c_1 = ComplexNumber(1, -2)
c_2 = ComplexNumber(3, 4)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)
