"""
Задание 8.4 Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина
брони персонажа). Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по
формуле damage / armor. Следовательно, у вас должно быть 2 функции:
- Наносит урон. Это улучшенная версия функции из задачи 3.
- Вычисляет урон по отношению к броне.
"""

player = {'name': input('Введите имя игрока:'), 'health': 1000, 'damage': 60, 'armor': 1.6}
enemy = {'name': input('Введите имя игрока:'), 'health': 1000, 'damage': 80, 'armor': 1.2}


def return_damage(person1, person2):
    back_damage = round((person1['damage'] / person2['armor']))
    return (back_damage)


def attack(person1, person2):
    new_health = person2['health'] - person1['damage']
    person2['health'] = new_health
    person1['health'] = person1['health'] - return_damage(player, enemy)
    print(
        f"Игрок {person1['name']} нанёс {person1['damage']} урона; у игрока {person2['name']} осталось {new_health} жизней; "
        f"игрок {person1['name']} получил {return_damage(player, enemy)} урона в обратку.")
    return person2['health']


attack(player, enemy)
