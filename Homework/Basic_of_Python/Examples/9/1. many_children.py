class Transport:
    def transport_method(self):
        print("Родительский метод класса Transport")


class Auto(Transport):
    def auto_method(self):
        print("Дочерний метод класса Auto")


class Bus(Transport):
    def bus_method(self):
        print("Дочерний метод класса Bus")


a = Auto()
a.transport_method()
b = Bus()
b.transport_method()