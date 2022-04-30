from math import pi


class Figure:
    units = "m^2"

    def __init__(self):
        self._area = 0

    def __str__(self):
        return f"{self.__class__.__name__} ({self.area:.3f} {self.units})"

    @property
    def area(self):
        if not self._area:
            self._area = self.calc_area()
        return self._area

    def calc_area(self):
        raise NotImplementedError(self.__class__.__name__)

    def __add__(self, other):
        result = Figure()
        result._area = self.area + other.area
        return result


class Box(Figure):
    def __init__(self, w, h):
        super().__init__()
        self._w = float(w)
        self._h = float(h)

    def calc_area(self):
        return self._w * self._h


class Circle(Figure):
    def __init__(self, r):
        super().__init__()
        self._r = float(r)

    def calc_area(self):
        return pi * self._r ** 2


class Square(Figure):
    def __init__(self, a):
        super().__init__()
        self._a = float(a)

    def calc_area(self):
        return self._a ** 2


if __name__ == '__main__':
    box_1 = Box("100", "200")
    square_1 = Square(100)
    circle_1 = Circle(20)
    print(box_1)
    print(square_1)
    print(circle_1)
    print(box_1 + square_1 + circle_1)
