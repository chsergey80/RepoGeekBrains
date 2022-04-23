# Пример работы с файлами
"""
file_1 = open('hello.txt', 'r', encoding='utf-8')

content = file_1.read()
print(content)   # content - тип "str"
print(dir(file_1))

clean_content = content.replace('\n', ' ').replace('\r', ' ')
print(clean_content)

paragraphs = content.splitlines()  # или можно так построить выражение: paragraphs = file_1.readlines()
print(paragraphs)   # paragraphs - тип list

# При работе с текстовыми файлами можем использовать метод .readline() файлового объекта для чтения одной строки:
print(file_1.readline())
print(file_1.readline())
print(file_1.readline())

# можно организовать цикл # построчного чтения файла:
line = file_1.readline()
while line:
    print(line)
    line = file_1.readline()

# в Python подобные манипуляции лучше делать через цикл-итератор, поэтому предпочтительнее следующий код:
for line in file_1:
    print(line)

file_1.close()
"""
"""
# Запишем код с использованием Менеджера контекста:

with open('hello.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        print(line)
"""
# Записываем информацию в файл методом .write() - сохраняет весь текст как одно целое
txt = '''Пробуем записать в файл текст.
Используем метод .write().'''
with open('write_method.txt', 'w', encoding='utf-8') as f:
    f.write(txt)              # В результате выполнения кода в папке урока должен появиться файл write_method.txt

# Записываем информацию в файл методом .write() в режиме 'а'

txt = '''Пробуем дозаписать в файл текст.
Режим доступа "a"'''
with open('append_text.txt', 'a', encoding='utf-8') as f:
    f.write(txt)

# Записываем информацию в файл методом .write() в режиме 'r+'. Нужно создать пустой файл replace_text_1.txt. В режиме
# ‘r+’ файл # автоматически не создаётся! Выполним скрипт:
txt = '''Пробуем дозаписать в файл текст.
Режим доступа "r+"
'''
with open('replace_text_1.txt', 'r+', encoding='utf-8') as f:
    f.write(txt)

# Записываем информацию в файл методом .writelines() - сохраняет список строк
txt_lines = ['Пробуем записать в файл текст.\n',
             'Используем метод .writelines().']
with open('writelines_method.txt', 'w', encoding='utf-8') as f:
    f.writelines(txt_lines)   # В результате выполнения кода в папке урока должен появиться файл writelines_method.txt

# Ещё один эксперимент. Создаём пустой файл replace_text_2.txt и выполняем один раз скрипт:
txt = '''Пробуем дозаписать в файл текст.
Режим доступа "r+"
'''
with open('replace_text_2.txt', 'r+', encoding='utf-8') as f:
    f.write(txt)
txt = '''Пробуем ДОЗАПИСАТЬ в файл текст!
Режим ДОСТУПА
'''
with open('replace_text_2.txt', 'r+', encoding='utf-8') as f:
    f.write(txt)


