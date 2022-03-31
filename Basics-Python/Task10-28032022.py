"""
Задание 8.3 Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:

    name - строка полученная от пользователя,
    health = 100,
    damage = 50.
    Поэкспериментируйте с значениями урона и жизней по желанию. Теперь надо создать функцию attack(person1, person2).
    Примечание: имена аргументов можете указать свои. Функция в качестве аргумента будет принимать атакующего и атакуемого.
    В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
    Функция должна сама работать со словарями и изменять их значения.
"""

def attack(person1, person2):
    new_health = person2['health'] - person1['damage']
    person2['health'] = new_health
    print(
        f"Игрок {person1['name']} нанёс {person1['damage']} урона; у игрока {person2['name']} осталось {new_health} жизней.")
    return person2['health']


player = {'name': input('Введите имя игрока:'), 'health': 1000, 'damage': 60}
enemy = {'name': input('Введите имя игрока:'), 'health': 1000, 'damage': 80}
attack(player, enemy)
