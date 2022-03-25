"""
Задание 6.1 В этой игре человек загадывает число, а компьютер пытается его угадать.
В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги. Компьютер начинает его
отгадывать предлагая игроку варианты чисел. Если компьютер угадал число, игрок выбирает “победа”. Если компьютер назвал
число меньше загаданного, игрок должен выбрать “загаданное число больше”. Если компьютер назвал число больше, игрок
должен выбрать “загаданное число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число.
Пример игры: Допустим, пользователь загадал число 42

`15
    35
    96
    <
    37
    74
    <
    52
    <
    42
    =`
Примечание: Знаки “=”, “>” и “<” пользователь вводит с клавиатуры для общения с компьютером.
Вы можете использовать этот способ или придумать свой.
"""

import random
user_number = int(input('Загадайте число от 1 до 100: '))
count = int(input('Сколько попыток вы хотите дать компьютеру? '))
a = 1
z = 100
i = 0
while i < count:
    i += 1
    if i > count:
        print('Компьютер потратил все попытки и не смог отгадать число ')
        break
    comp_number = random.randint(a, z)
    print(comp_number)
    if user_number == comp_number:
        print("Компьютер смог отгадать число! - " + str(comp_number))
        break
    if user_number > comp_number:
        a = comp_number
    if user_number < comp_number:
        z = comp_number