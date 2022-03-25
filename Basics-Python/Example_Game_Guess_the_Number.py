import random
number = random.randint(1, 100)  # Возвращает случайное целое число в заданом диапазоне
print(number)
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}     # Создаем справочник с данными об уровнях сложности
level = int(input('Введите уровень сложности: '))
max_count = levels[level]        # Вызываем из словаря данные по характеристикам уровня
user_count = int(input('Введите количество пользователей: '))
users = []                       # Создаем список с именами участников игры
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i}')
    users.append(user_name)
print(users)
is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('Вы проиграли')
        break
    print(f'Попытка № {count}')
    user_number = int(input('Введите число: '))
    for user in users:
        print(f'Ход пользователя {user}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Ваше число больше загаданного ')
        else:
            print('Ваше число меньше загаданного ')
else:
    print(f'Победитель {winner_name}')