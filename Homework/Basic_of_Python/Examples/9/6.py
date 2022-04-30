class User:
    def __init__(self, name):
        self._name = name


class Admin(User):
    pass


user_1 = User('Иван')
user_2 = Admin('Петр')

# даже пустой класс можно полезно использовать
if isinstance(user_2, Admin):
    print("Доступ разрешен")
if type(user_2) == Admin:
    print("Доступ разрешен")

