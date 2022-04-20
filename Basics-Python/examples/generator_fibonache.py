# Например, генерация чисел Фибоначчи

import sys


def nums_generator(max_num):


    for num in range(1, max_num + 1, 2):
        yield num ** 2

nums_gen = nums_generator(10 ** 6)
print(type(nums_gen), sys.getsizeof(nums_gen))
print(sum(nums_gen))
