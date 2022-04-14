"""
Задание 5.5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список
с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""

import time
import sys


def my_set(*argv):
    answ = set()
    for elem in argv:
        if not elem in answ:
            answ.add(elem)
        else:
            answ.remove(elem)
    return [x for x in argv if x in answ]


if __name__ == "__main__":
    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [23, 1, 3, 10, 4, 11]
    t = time.perf_counter()
    r = my_set(*src)
    print("mem: ", sys.getsizeof(r))
    print("time: ", time.perf_counter() - t)
    print(r == result)
    print(r)
