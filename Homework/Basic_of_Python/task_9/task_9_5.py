"""
Задание 9.5. Реализовать класс Stationery (канцелярская принадлежность).
- определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
- создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
- в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
- создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    title: str

    def draw(self) -> None:
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "ручка"

    def draw(self) -> None:
        print("Пишем текст")
        return None


class Pencil(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "карандаш"

    def draw(self) -> None:
        print("Чертим чертеж")
        return None


class Handle(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "маркер"

    def draw(self) -> None:
        print("Выделяем заголовки")
        return None


if __name__ == "__main__":
    pen = Pen()
    pencil = Pencil()
    handle = Handle()

    for some in [pen, pencil, handle]:
        print(f"{some.__class__}:title = {some.title}")
        print(f"{some.__class__}.draw() =>\t", end="")
        some.draw()
        print()
