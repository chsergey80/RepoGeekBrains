# Еще один пример генератора

from itertools import islice

nums = []
nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))

print(next(nums_gen), next(nums_gen), next(nums_gen), sep=', ')
print(*islice(nums_gen, 3))

nums_gen_sum = sum(nums_gen)
print(nums_gen_sum)

# После вызова функции sum() мы получили сумму ОСТАВШИХСЯ элементов последовательности и всё.
# Больше генерировать нечего — поэтому при повторной попытке посчитать сумму получили ноль.
nums_gen_sum = sum(nums_gen)
print(nums_gen_sum)

# Вывод: если последовательность нужна в алгоритме более одного раза, использование генератора
# может быть неэффективным или приводить к ошибкам.


# Генератор английских букв

eng_letters_gen = (chr(code) for code in range(ord('a'), ord('z') + 1))
print(*eng_letters_gen, sep='')
