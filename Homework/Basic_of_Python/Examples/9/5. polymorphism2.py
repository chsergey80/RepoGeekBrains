class Transport:
    def show_info(self):
        print("Родительский метод класса Transport")


class Auto(Transport):
    def show_info(self):
        print("Дочерний метод класса Auto")
        super().show_info()


class Bus(Transport):
    def show_info(self):
        print("Дочерний метод класса Bus")
        Transport.show_info(self)


t = Transport()
t.show_info()

a = Auto()
a.show_info()

b = Bus()
b.show_info()