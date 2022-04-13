names = ('Иван', 'Анна', 'Игорь', 'Иван', 'Сергей', 'Анна')
new_names = ('Андрей', 'Пётр', 'Иван', 'Сергей')
my_set = {names, new_names}
name = 'Пётр'
i = 0
for tpl in my_set:  # O(m) -> O(m * n)
    if name in tpl: # O(n)
        i += 1
print(i)




