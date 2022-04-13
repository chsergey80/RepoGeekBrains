names = ['Иван', 'Анна', 'Игорь', 'Иван', 'Сергей', 'Анна']
# for name in names:  # O(n ** 2)
#     if names.count(name) == 1:
#         print(name)

unique_names = set()
repeated_names = set()
for name in names:  # O(n)
    if name in repeated_names:
        continue
    if name in unique_names:
        unique_names.discard(name)  # не выдаёт исключение
        repeated_names.add(name)
        continue
    unique_names.add(name)
print([name for name in names if name in unique_names])    #O(n)


