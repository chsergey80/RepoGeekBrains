"""
Задание 10.2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
"""
from random import choice

def spisok(new_list):
    if new_list:
        result = choice(new_list)
        return result

list_1 = [1, 2, 3, 4]
list_2 = []

if __name__ == '__main__':
    print(spisok(list_1))
    print(spisok(list_2))