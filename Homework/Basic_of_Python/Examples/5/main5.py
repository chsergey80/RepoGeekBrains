names = {'Иван', 'Анна', 'Игорь', 'Иван', 'Сергей', 'Анна'}
new_names = {'Андрей', 'Пётр', 'Иван', 'Сергей'}
my_tpl = (names, new_names)
name = 'Пётр'
i = 0
for st in my_tpl:  # O(m) -> O(m)
    if name in st: # O(1)
        i += 1
print(i)
