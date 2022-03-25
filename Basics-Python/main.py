import random

min_number = int(input('Введите минимально допустимое число в выборке'))
max_number = int(input('Введите максимально допустимое число в выборке'))
zapros = None
while zapros != '=':
    number = random.randint(min_number, max_number)
    print(number)
    zapros = input(' => (загаданное число больше вышего)  <')
    if zapros == '>':
        min_number = number + 1
    elif zapros == '<':
        max_number = number - 1
print('Выигрыш')

