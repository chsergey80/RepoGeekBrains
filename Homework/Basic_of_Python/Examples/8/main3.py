from time import perf_counter
from functools import wraps


def decorate_profile(callback):
    @wraps(callback)
    def wrapper(*args):
        start = perf_counter()
        area = callback(*args)
        time_cost = perf_counter() - start
        print(f'{time_cost:.7f}')
        return area
    return wrapper       # После wrapper скобки не ставятся


@decorate_profile       # При вызове функции calc_box декоратор (его название указано после знака @) вызывается автоматически
def calc_box(w, h):    # Наша основная функция
    'Calculates box area'
    return w * h 


def calc_box_profile(w, h):
    start = perf_counter()
    area = calc_box(w, h)
    time_cost = perf_counter() - start 
    print(f'{time_cost:.3f}')
    return area 


def profile(callback, *args):    # передаем в callback нужную нам функцию как аргумент (например, расчета площади)
    start = perf_counter()
    area = callback(*args)       # та самая функция
    time_cost = perf_counter() - start 
    print(f'{time_cost:.3f}')
    return area 


area_1 = calc_box(150, 5)  # При наличии декоратора, вызывается не функция calk_box, а декоратор, который вызывает эту функцию.
print(area_1)

area_2 = calc_box_profile(150, 5)
print(area_2)

area_3 = profile(calc_box, 150, 5)
print(area_3)

help(calc_box)