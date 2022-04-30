class Transport:
    # атрибуты класса
    # name = 'Lexus'
    # model = 'RX350L'
    # year = 2022
    color = 'Black'
    a_count = 0

    # конструктор (инициализатор) и атрибуты экземпляра
    def __init__(self, name, model, year=2022):
        self.name = name
        self._model = model
        self.__year = year
        # Auto.a_count += 1
        # self.id = Auto.a_count
        self.on_start(100)

    # методы класса
    def on_start(self, speed=65):
        print(f"Go-go car {self.name} with speed {speed}!")
        self.on_stop()

    def on_stop(self):
        print("Stop!")


class Auto(Transport):
    def __init__(self, name, model, year=2022, p_v=4):
        super().__init__(name, model, year)
        self.p_v = p_v

    def on_start(self, speed=100):
        super().on_start(speed)

    def drift(self):
        print("Vgg!")


auto_1 = Auto('BMW', "S7")
auto_2 = Auto('Запорожец', 'ВАЗ-100500', 2021, 6)
auto_1.on_start()
auto_1.drift()
# print(auto_1.name)
# auto_1.name = 'Mazda'
# print(auto_1.name)
# print(auto_2.name)
# print(auto_1.color)
# print(vars(auto_1))
# print(auto_1.a_count)
# print(auto_2.a_count)
# print(auto_1.id)
# print(auto_2.id)
# Auto.on_start()
# print(auto_1._model)
# auto_1._model = 'S100500'
# print(auto_1._model)
# print(auto_1.__year)
# auto_1.__year = 100500
# print(auto_1.__year)
# print(auto_1._Auto__year)
