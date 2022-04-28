"""
Задание 6.3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что
 при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
 Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
 Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в
 файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):

Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):

скалолазание,охота
горные лыжи

"""
import os
import json

def my_zip_gen(a_iter, b_iter):
    len_b = len(b_iter)
    return ((a_elem, b_iter[i]) if i < len_b else (a_elem, None)
            for i, a_elem in enumerate(a_iter))


def groping(output_pth="./out.txt", user_pth="./users.csv", hobby_pth="./hobby.csv"):
    if not (os.path.isfile(user_pth) or
            os.path.isfile(hobby_pth)):
        return -1
    user_lines = None
    hobby_lines = None
    with open(user_pth, "r", encoding="utf-8") as user_file:
        user_lines = user_file.readlines()
    with open(hobby_pth, "r", encoding="utf-8") as hobby_file:
        hobby_lines = hobby_file.readlines()
    if len(user_lines) < len(hobby_lines):
        return 1
    group = {}
    for fio, hobby in my_zip_gen(user_lines, hobby_lines):
        fio = fio.replace("\n", "").replace(",", " ")
        group[fio] = hobby.replace("\n", "") if hobby else None
    with open(output_pth, 'w+', encoding='utf-8') as out_file:
        out_file.writelines(json.dumps(group))
    return group

if __name__ == "__main__":
    exit(groping())
