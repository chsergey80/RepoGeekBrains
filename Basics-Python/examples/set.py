# Задачи по множествам.
# Базовая структура типа данных “множество”, это хеш-таблица (Hash Table). Поэтому множества очень быстро справляются с
# проверкой элементов на вхождение, например содержится ли объект x в последовательности a_set.
# Идея заключается в том, что поиск элемента в хэш-таблице это операция O(1), т.е операция с постоянным временем выполнения.

# Как не надо делать(из-за цикличности - долго):

names = ['Иван', 'Анна', 'Игорь', 'Иван', 'Сергей', 'Анна', 'Василий', 'Вася']
for name in names:  # Сложность О(n**2)
    if names.count(name) == 1:
        print(name)

# Запишем программу на основе множеств:

unique_nameas = set()
repeated_names = set()
for name in names: # О(1)
    if name in repeated_names:
        continue
    if name in unique_nameas:
        unique_nameas.discard(name)   # не выдает исключение
        repeated_names.add(name)
        continue
    unique_nameas.add(name)
print([name for name in names if name in unique_nameas])   # О(n)

# Еще задача на пересечение множеств

names = {'Иван', 'Анна', 'Игорь', 'Иван', 'Сергей', 'Анна', 'Василий', 'Вася'}
new_names = {'Андрей', 'Пётр', 'Иван', 'Сергей'}
print(names.intersection(new_names))    # пересечение множеств
print(names & new_names)

print(names.union(new_names))    # объединение множеств
print(names | new_names)

print(names - new_names)    # вычитание множеств

