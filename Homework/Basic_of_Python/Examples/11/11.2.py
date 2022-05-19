class UserAttribError(Exception):
    pass


class User:
    special_attrs = []
    validated_attrs = {}

    def __init__(self, username):
        self.username = username

    @classmethod
    def create(cls, username, **kwargs):
        kwargs = cls._validator2(**kwargs)  # валидация типов аргументов
        instance = cls(cls._validator(username))  # валидация имени пользователя и создание валидного объекта
        for attrib in cls.special_attrs:
            setattr(instance, attrib, kwargs.get(attrib))  # установка значений атрибутов
        return instance

    @staticmethod
    def _validator(username):
        if not username:
            raise ValueError("wrong username")
        return username

    @classmethod
    def _validator2(cls, **kwargs):
        for attrib, attr_type in cls.validated_attrs.items():
            if not isinstance(kwargs.get(attrib), attr_type):
                raise UserAttribError(f"wrong {attrib} type")
        return kwargs


class SuperUser(User):
    special_attrs = ["level"]
    validated_attrs = {"level": int}

    @staticmethod
    def _validator(username):
        if not username or len(username) < 5:
            raise ValueError("wrong username")
        return username


class StaffUser(User):
    special_attrs = ['speciality', 'security_access']
    validated_attrs = {"security_access": bool}


def main():
    try:
        user_1 = SuperUser.create("Иваныч", level=5)
        user_2 = StaffUser.create("Пётр", speciality="db admin", security_access=True)
    except UserAttribError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(vars(user_1))
        print(vars(user_2))


if __name__ == '__main__':
    main()