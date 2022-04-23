"""
Задание 6.6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки
значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:

    просто запуск скрипта — выводить все записи;
    запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
    запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму
    числу, включительно.

Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.

Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:

python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
"""
import sys


def file_reader(start=-1, end=-1):
    with open('bakery.csv', "r", encoding="utf-8") as price_list:
        # skip
        if start > 0:
            for _ in range(start - 1):
                price_list.readline()
        # stop
        if end > 0:
            for _ in range(abs(end - start) + 1):
                yield price_list.readline().replace("\n", "")
        else:
            for line in price_list:
                yield line.replace("\n", "")


if __name__ == "__main__":
    start_pos = -1
    end_pos = -1
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        start_pos = int(sys.argv[1])
    if len(sys.argv) == 3 and sys.argv[2].isdigit():
        end_pos = int(sys.argv[2])
    for l in file_reader(start_pos, end_pos):
        if l != '':
            print(f"{float(l):.2f}")

