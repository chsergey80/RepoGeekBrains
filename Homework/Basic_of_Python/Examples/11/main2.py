class MyClass:
    """My documentation"""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @classmethod
    def set_name(cls, data):
        name, surname = data
        return cls(name, surname)

    @staticmethod
    def get_name(self):
        return f"{self.name} {self.surname}"


my_1 = MyClass("Ivan", "Ivanov")
# print(my_1.surname)
#
# my_list = ['Maria', 'Lapteva']
# my_2 = MyClass.set_name(my_list)
# print(my_2.surname)
#
# print(my_2.get_name(my_2))

# print(MyClass.__name__)
# print(MyClass.__module__)
# print(MyClass.__doc__)
# print(MyClass.__init__)
# print(MyClass.__dict__)
# print(MyClass.__bases__)
# print(MyClass.__mro__)
# print(vars(MyClass))
# help(MyClass)
print(my_1.__class__.__name__)
print(my_1.__class__.__module__)
print(my_1.__class__.__doc__)
print(my_1.__class__.__init__)
print(my_1.__class__.__dict__)
print(my_1.__class__.__bases__)
print(my_1.__class__.__mro__)