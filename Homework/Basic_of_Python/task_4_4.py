"""
Задание 4.4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
"""

import utils

while True:
    code = input('Введите код валюты или q для выхода: ')
    if not code == 'q':
        print(utils.currency_rates(code))
    else:
        break
