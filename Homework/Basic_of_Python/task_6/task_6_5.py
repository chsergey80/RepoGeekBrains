"""
Задание 6.5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к
обоим исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы
находятся в разных папках.
"""

import sys


def groping(user_pth, hobby_pth, output_pth):
    with open(user_pth, 'r', encoding='utf-8') as f1, \
            open(hobby_pth, 'r', encoding='utf-8') as f2, \
            open(output_pth, 'w', encoding='utf-8') as f3:
        for line_1 in f1:
            line_2 = f2.readline().strip()
            if not line_2:
                line_2 = None
            f3.write(f'{line_1.strip()}: {line_2}\n')
        content = f2.readline()
        if content:
            sys.exit(1)


if __name__ == "__main__":
    user_name = ""
    hobby_name = ""
    output_name = ""
    print(len(sys.argv[:]))
    if len(sys.argv[1:]) >= 3:
        user_name = sys.argv[1]
        hobby_name = sys.argv[2]
        output_name = sys.argv[3]
    if not user_name:
        user_name = "./users.csv"
    if not hobby_name:
        hobby_name = "./hobby.csv"
    if not output_name:
        output_name = "./report.txt"
    exit(groping(user_pth=user_name, hobby_pth=hobby_name, output_pth=output_name))
