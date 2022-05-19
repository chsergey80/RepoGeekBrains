class Transport(object):
    # атрибуты класса - переменные, которые хранят данные, характеризующие все экземпляры класса.
    # name = 'Lexus'
    # model = 'RX350L'
    # year = 2022
    color = 'Black'
    a_count = 0

    # конструктор (инициализатор) и атрибуты экземпляра

    def __init__(self, name, model, year=2022):
        self.name = name     # публичные данные
        self._model = model  # защита данных
        self.__year = year   # Приватные данные
        # Avto.a_count += 1
        # self.id = Avto.a_count
        self.on_start(100)


    # методы класса
    def on_start(self, speed=65):
        print(f'go-go car {self.__year} with speed {speed}!')

    def on_stop(self):
        print("Stop!")


class Auto(Transport):
    pass


auto_1 = Auto('BMV', 'S7', 2021)
auto_2 = Auto('Запорожец','ВАЗ-100500')
auto_1.on_start()
# print(auto_1.name)
# auto_1.name = 'Mazda'
# print(auto_1.name)
# print(auto_2.name)
# print(auto_1.color)
# print(auto_1.a_count)
# print(auto_2.a_count)
# print(auto_1.id)
# print(auto_2.id)
# Avto.on_start()
# print(auto_1._model)
# auto_1._model = 'S100500'
# print(auto_1._model)
# print(auto_1.__year)   # не выводит значение, поскольку нарушается принцип инкапсуляции, __year - приватная переменная
# auto_1.__year = 100500
# print(auto_1.__year)
print(auto_1._Auto__year)