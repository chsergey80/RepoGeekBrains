"""
Задание 10.3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
Вызовите каждую функцию в main.py и проверьте что все работает как надо.
Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.
"""
from Task12_31032022 import makedir, deldir
import Task13_02042022

makedir()
deldir()

list_1 = [1, 2, 3, 4]
list_2 = []

print(Task13_02042022.spisok(list_1))
print(Task13_02042022.spisok(list_2))