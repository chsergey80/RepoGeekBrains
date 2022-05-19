class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PhoneMixin:
    screen_size = None

    def get_screen_size(self):
        return self.screen_size


class Phone(PhoneMixin, Product):
    pass