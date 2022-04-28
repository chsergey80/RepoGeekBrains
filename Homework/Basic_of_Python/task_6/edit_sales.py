"""
Задание 6.7  * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему
номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование. Предусмотреть
ситуацию, когда пользователь вводит номер записи, которой не существует.
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
"""

import sys

if __name__ == "__main__":
    if len(sys.argv[1:]) != 2:
        sys.exit(1)
    pos = sys.argv[1]
    new_price = sys.argv[2]
    if not (pos.isdigit() and new_price.replace(".", "").isdigit()):
        sys.exit(1)
    pos = int(pos)
    new_price = float(new_price)
    with open('bakery.csv', "r+", encoding="utf-8") as price_list:
        skip_chars = 0
        for line in range(pos - 1):
            try:
                skip_chars += len(next(price_list))
            except StopIteration:
                print("out of index")
                sys.exit(1)
        price_list.seek(skip_chars + 2)
        print(new_price)
        price_list.writelines(f"{new_price}")
