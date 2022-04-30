class Product:
    def __init__(self, price, name=""):
        self._price = price
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__} {self.name} with price {self._price}"

    def __add__(self, other):  # (self + other) -> self + other (Product_3)
        return Product(self._price + other._price)

    def __radd__(self, other):  # other + self
        if not isinstance(other, Product):  # if type(other) != Product
            return self
        return self.__add__(other)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = float(value)

    def __getattribute__(self, item):
        print(f"__getattribute__ {item}")
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print(f"__getattr__ {item}")
        return ":)"


class Notebook(Product):
    def __init__(self, price, name, brand):
        super().__init__(price, name)
        self._brand = brand


class Tablet(Product):
    def __init__(self, price, name, screen_type):
        super().__init__(price, name)
        self.screen_type = screen_type


class Basket:
    def __init__(self):
        self._products = []
        self._cost = None

    def add(self, product):
        self._products.append(product)
        self._cost = None

    def remove(self, product):
        if product in self._products:
            self._products.remove(product)
            self._cost = None

    @property
    def cost(self):
        if self._cost is None:
            print("calc cost")
            self._cost = sum(self._products)
        return self._cost

    def __iter__(self):
        print("ITER")
        return (el for el in self._products)

    def __contains__(self, item):
        print("IN")
        return item in self._products


product_1 = Notebook(58999, "Aspire", "Acer")
product_2 = Notebook(97560, "Matebook", "Huawei")
product_3 = Tablet(78549, "iPad Air", "IPS")

# print(product_1)
#
# # basket_price = product_1._price + product_2._price + product_3._price
# # print(basket_price)
# basket_price = product_1 + product_2 + product_3
# print(basket_price)
#
# basket = [product_1, product_2, product_3]
# #print(sum(basket, Product(0)))
# print(sum(basket))

# basket = Basket()
# basket.add(product_1)
# basket.add(product_2)
# basket.add(product_3)
# print(basket.cost)
# print(basket.cost)
# print(basket.cost)
#
# for item in basket:
#     print(item)
#
# print(product_1 in basket)

print(product_1.price)
print(product_2._brand)
print(product_3._brand)
# product_1.price = 35000
# print(product_1.price)