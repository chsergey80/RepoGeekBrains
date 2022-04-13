names = {'Иван', 'Анна', 'Игорь', 'Иван', 'Сергей', 'Анна'}
new_names = {'Андрей', 'Пётр', 'Иван', 'Сергей'}
print(names.intersection(new_names))  # пересечение
print(names & new_names)

print(names.union(new_names))  # объединение
print(names | new_names)

print(names - new_names)