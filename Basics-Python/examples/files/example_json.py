# Примеры сериализации при помощи модуля json / Формат JSON
"""
# Пример №1

import json
import random
nums = [random.randint(0, 100) for _ in range(12)]

nums_as_str = json.dumps(nums)  # выполняет задачу сериализации Python-объектов в соответствии с приведенной табл.типов
print(nums, type(nums))
print(nums_as_str, type(nums_as_str))

with open('nums.json', 'w', encoding='utf-8') as f:
    f.write(nums_as_str)
"""
"""
# Пример №2.

import json

with open('nums.json', 'r', encoding='utf-8') as f:
    nums_as_str = f.read()
nums = json.loads(nums_as_str)
print(nums, type(nums))
"""

# Пример №3.
import json
import random

nums = [random.randint(0, 100) for _ in range(10)]
with open('nums_again.json', 'w', encoding='utf-8') as f:
    json.dump(nums, f)                                    # Сохранение в файл
with open('nums_again.json', 'r', encoding='utf-8') as f:
    nums_new = json.load(f)                               # Загрузка из файла
print(nums, type(nums))
print(nums_new, type(nums_new))
