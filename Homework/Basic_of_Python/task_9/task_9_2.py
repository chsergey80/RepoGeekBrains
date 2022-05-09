"""
Задание 9.2. Реализовать класс Road (дорога).
- определить атрибуты: length (длина), width (ширина);
- значения атрибутов должны передаваться при создании экземпляра класса;
- атрибуты сделать защищёнными;
- определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
- использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна;
- проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""
class Road:

    _length: float
    _width: float

    def __init__(self, length: float = 0, width: float = 0) -> None:
        self._length = length
        self._width = width

    def calc(self, density: float, thickness: float) -> float:
        return self._length * self._width * density * thickness


if __name__ == "__main__":
    road = Road(length=20, width=5000)
    print(road.calc(25, 5))

    # or if we in module
    road = Road()
    road._length = 20
    road._width = 5000
    print(road.calc(density=25, thickness=5))
