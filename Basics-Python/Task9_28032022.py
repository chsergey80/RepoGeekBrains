"""
Задание 8.2  Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
"""


def sort_num(a, b, c):
    result = max([a, b, c])
    return result

result = sort_num(1, 5, 3)
print(result)

print(sort_num(1, 5, 3))
