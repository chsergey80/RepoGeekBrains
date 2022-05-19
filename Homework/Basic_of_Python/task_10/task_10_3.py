"""
Задание 10.3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__floordiv__, __truediv__()). Эти методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и округление до целого числа деления клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек
этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Этот метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order() вернёт
строку: *****\n*****\n**.
Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.simbol = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.cell}')

    def __sub__(self, other):
        return Cell(abs(self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def make_order(self, count):
        x = self.cell
        while x > 0:
            for k in range(1, count + 1):
                print(self.simbol, end='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end='')


a = Cell(5)
b = Cell(10)
c = Cell(3)
d = Cell(2)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(3)
b.make_order(3)
