# Есть ли в Python для словарей синтаксис, аналогичный List Comprehensions? Есть:

nums_cube = {num: num ** 3 for num in range(1, 5 + 1)}
print(nums_cube)

# Разница лишь в наличии символа “:”, разделяющего ключ и значение. Так выглядел бы обычный код для создания такого словаря:

nums_cube1 = {}
for num in range(1, 5 + 1):
    nums_cube1[num] = num ** 3
print(nums_cube1)

# Dict Comprehensions могут быть полезны для преобразования одного словаря в другой:

eng_ru = {'may': 'май', 'june': 'июнь', 'july': 'июль'}
ru_eng = {val: key for key, val in eng_ru.items()}
print(ru_eng)

# В чём коварство такой манипуляции? Надо быть уверенным, что значения, как и ключи, уникальны. Иначе потеряете часть
# элементов исходного словаря:

eng_ru_nums = {'one': 'один', 'first': 'один', 'two': 'два'}
ru_eng_nums = {val: key for key, val in eng_ru_nums.items()}
print(ru_eng_nums)
