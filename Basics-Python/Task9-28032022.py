"""
Задание 8.2  Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
"""

def sort_num():
    for i in range(3):
        number = int(input('Введите число'))
        numbers.append(number)
    print(max(numbers))
numbers = []
sort_num()