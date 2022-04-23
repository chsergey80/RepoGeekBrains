# Работа с бинарными файлами. Модуль pickle
"""
# Пример №1.   Решим задачу при помощи модулей json и pickle, при этом будем профилировать время:

import json
import pickle
import random
from time import perf_counter

nums = [random.random() * 10 ** 4 for _ in range(10 ** 4)]
start = perf_counter()
with open('random_million.json', 'w', encoding='utf-8') as f:
    json.dump(nums, f)                                        # Сохранение в файл
print(f'json saved: {perf_counter() - start}')
start = perf_counter()
with open('random_million.pickle', 'wb') as f:
    pickle.dump(nums, f)                                      # Сохранение в файл
print(f'pickle saved: {perf_counter() - start}')
"""
"""
# Пример №2.   Теперь загрузим данные:

import json
import pickle
from time import perf_counter

start = perf_counter()
with open('random_million.json', 'r', encoding='utf-8') as f:
    nums = json.load(f)
print(f'json loaded: {perf_counter() - start}, {type(nums)}, {len(nums)}')
start = perf_counter()
with open('random_million.pickle', 'rb') as f:
    nums = pickle.load(f)
print(f'pickle loaded: {perf_counter() - start}, {type(nums)}, {len(nums)}')
"""
"""
# Пример №3.

import pickle

chunk_size = 256
with open('random_million.pickle', 'rb') as f:
    binary_data = bytearray()   #Массив байт, использовали метод .extend() этого объекта. Т.е.это типизированный список.
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        binary_data.extend(chunk)
    nums = pickle.loads(binary_data)
print(f'{type(nums)}, {len(nums)}')
"""
"""
# Пример №4. класса str есть два # метода для преобразования в последовательность байт и наоборот:

txt = 'Привет,Python!'
txt_binary = txt.encode(encoding='utf-8')
txt_origin = txt_binary.decode(encoding='utf-8')
print(txt_binary, type(txt_binary))
print(txt_origin, type(txt_origin))
"""
