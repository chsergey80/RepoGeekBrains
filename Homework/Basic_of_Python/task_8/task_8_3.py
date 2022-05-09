"""
Задание 8.3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3
>>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""
from functools import wraps


def type_logger(level=0):
    def logger(func):
        @wraps(func)
        def decor(*argv, **kwargs):
            all_args = list(argv) + list(kwargs.values())
            norm_res = func(all_args[0])
            if level == 1:
                print(", ".join([f"{x}:{type(x)}" for x in all_args]))
            elif level == 2:
                print(f"{func.__name__}:{type(func)}")
                print(f"{func.__name__}({all_args[0]}):{type(norm_res)}")
            return norm_res
        return decor
    return logger


@type_logger(2)
def calc_cube(x):
    return x ** 3

if __name__ == "__main__":
    a = calc_cube(5, 6, 7, 8, 9, 1, 2, 3, val1=4, val2=5)
    print(a)
