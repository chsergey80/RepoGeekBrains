class Auto:
    def __init__(self, year):
        self.year = year

    # создаём свойство года
    @property
    def year(self):
        return self.__year

    # сеттер для создания свойств
    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2022:
            self.__year = 2022
        else:
            self.__year = year

    def get_auto_year(self):
        return f"Автомобиль выпущен в {str(self.year)} году."


a1 = Auto(2090)
print(a1.get_auto_year())
a2 = Auto(1090)
print(a2.get_auto_year())
a3 = Auto(2010)
print(a3.get_auto_year())
a3.year = 2100  # ветвление в конструкторе тут бы не помогло
print(a3.get_auto_year())

