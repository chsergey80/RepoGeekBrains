# Примеры работы с модулем os
# Пример 1.
#import os


#folder = r'C:\Documents\RepoGeekBrains\Basics-Python'
# py_files = [item for item in os.listdir(folder) if item.lower().endswith('.py')]
# print(py_files)
# print(dir(py_files))
# print(type(py_files))

#py_files = [os.path.join(folder, item) for item in os.listdir(folder)
#            if item.lower().endswith('.py')]   # Метод str.endswith() - Поиск строк с заданным суффиксом/окончанием
#print(py_files)

#django_dirs = [item for item in os.listdir(folder)
#              if os.path.isdir(os.path.join(folder, item))]
#print(django_dirs)

# Пример 2. Создадим в корне урока папку some_data, а в ней 1000 небольших файлов разного размера. Можно сделать это при помощи скрипта:
# import os
# import random
#
# folder = 'some_data'
# letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
# for _ in range(10 ** 3):
#     f_name = ''.join(random.sample(letters, random.randint(5, 10)))
#     f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5)))
#     with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
#         f.write(f_content)

# Пример 3. Теперь решим задачу: вывести на экран имена и размер файлов размером не более 15 КБ.
# import os
# from time import perf_counter
#
# folder = 'some_data'
# start = perf_counter()
# size_threshold = 15 * 2 ** 10
# small_files = [item for item in os.listdir(folder) if os.stat(os.path.join(folder, item)).st_size < size_threshold]
# print(len(small_files), perf_counter() - start)
#
# start = perf_counter()
# small_files_2 = [item.name for item in os.scandir(folder) if item.stat().st_size < size_threshold]
# print(len(small_files_2), perf_counter() - start)
# print(small_files == small_files_2)

# Пример 4. Теперь решим первую задачу — просто получим список # файлов в папке:
# import os
# from time import perf_counter
#
# folder = 'some_data'
# start = perf_counter()
# all_files = [item for item in os.listdir(folder)]
# print(len(all_files), perf_counter() - start)
# start = perf_counter()
# all_files_2 = [item.name for item in os.scandir(folder)]
# print(len(all_files_2), perf_counter() - start)
# print(all_files == all_files_2)

# Пример 5.
# import os
#
# root = r'C:\Users\User\AppData\Local\Programs\Python\Python310\Lib\site-packages\django'
# folder = r'C:\Users\User\AppData\Local\Programs\Python\Python310\Lib\site-packages\django\contrib\admin'
# django_admin_dirs = [os.path.relpath(item, root) for item in os.scandir(folder)
#         if item.is_dir() and not item.name.startswith('_')]
# print(django_admin_dirs)

# Пример 6.
# import os
#
# root = r'C:\Users\User\AppData\Local\Programs\Python\Python310\Lib\site-packages\django'
# curr_file = r'C:\Users\User\AppData\Local\Programs\Python\Python310\Lib\site-packages\django\http\request.py'
# print('exists', os.path.exists(curr_file))
# f_dir, f_name = os.path.split(curr_file)   # делит путь к файлу на путь к папке и имя файла
# print(f_dir, f_name, sep=' | ')
# print('dirname ok', f_dir == os.path.dirname(curr_file))
# print('basename ok', f_name == os.path.basename(curr_file))
# print('abspath ok', curr_file == os.path.abspath(curr_file))
# curr_file_rel = os.path.relpath(curr_file, root)
# print(curr_file_rel)
# print('relpath ok', curr_file == os.path.join(root, curr_file_rel))

# Пример 7. Модуль os: создание, переименование и удаление папок
# import os

# dir_name = 'sample_dir'
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)

# dir_path = os.path.join('data', 'src')
# if not os.path.exists(dir_path):
#     os.mkdir(dir_path)   # Создаем одну папку

# dir_path = os.path.join('data', 'src')
# if not os.path.exists(dir_path):
#     os.makedirs(dir_path)   # Создаем несколько папок

# dir_name = 'first_dir'
# new_dir_name = '../first_out_dir'
# if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
#     os.rename(dir_name, new_dir_name)   # Переименовываем существующую папку

# to_remove_dir_name = 'second_dir'
# if os.path.exists(to_remove_dir_name):   # Проверка на наличие папки
#     os.rmdir(to_remove_dir_name)        # Удаление папки

# Пример 8. Работа с файловой системой: модуль shutil

# import os
# import shutil
#
# to_remove_dir_name = 'second_dir'
# if os.path.exists(to_remove_dir_name):
#     shutil.rmtree(to_remove_dir_name)

# Пример 9. Реализация функции copyfileobj()

# import random
# import shutil
#
#
# for _ in range(3):
#     with open('hello.txt', encoding='utf-8') as src:
#         with open('summary.txt', 'a', encoding='utf-8') as dst:
#             head_size = random.randrange(21)
#             print(head_size, src.read(head_size), src)
#             shutil.copyfileobj(src, dst)
#     print(shutil.copyfile())


# Пример 10.
# import os
# from shutil import copyfile, copy, copy2
#
#
# def show_stat(f_path):
#     stat = os.stat(f_path)
#     print('{f_p}:\n\tperm - {perm}, modify {m_t:.0f}, access {a_t:.0f}'.format(
#         f_p=f_path,
#         perm=oct(stat.st_mode),
#         m_t=stat.st_mtime,
#         a_t=stat.st_atime,
#     ))
# src = 'summary.txt'
# show_stat(src)
# show_stat(copyfile(src, 'new_data/summary_clone.txt'))
# show_stat(copy(src, 'new_data'))
# show_stat(copy2(src, 'new_data/summary_clone_2.txt'))


# Пример 11.

import os
from collections import defaultdict
from os.path import relpath
import django
root_dir = django.__path__[0]
django_files = defaultdict(list)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        rel_path = relpath(os.path.join(root, file), root_dir)
        django_files[ext].append(rel_path)
for ext, files in sorted(django_files.items(), key=lambda x: len(x[1]), reverse=True):
    print(f'{ext}: {len(files)}')
print('\nPY FILES')
print(*sorted(django_files['py'])[:10], sep='\n')


# Пример 12.




# Пример 2.
#import shutil

"""
import os

root_dir = './'
for item in os.scandir(root_dir):
    print(type(item))
    print(item.is_dir())
    print(item.is_file())
    print(item.stat().st_size)
"""
# Пример 3.
"""
import os

root_dir = './'
for root, dirs, files in os.walk(root_dir):
    #print(root)   #Это иерархия папок текущей папки
    #print(dirs)    #Это подпапки папки root
    #print(files)    #Это имена файлов, находящихся внутри папки root
    #print(type(root))
    for file in files:
        #print(f'{root}/{file}')  # Этот вариант нельзя считать кроссплотформенным\
        f_path = os.path.join(root, file)  # Так получается кроссплатформенно
        #print(f_path)
        print(os.path.exists(f_path))
        print(os.stat(f_path).st_size)
        print(os.path.split(f_path))  # Разбивает путь (папки) и название файла - способ первый
        print(os.path.dirname(f_path), os.path.basename(f_path))  # Разбивает путь (папки) и название файла - способ первый
"""
# Пример 4.
"""
print(__file__)  # так можно вывести путь к вайлу программы, которую мы запускаем
ROOT = os.path.dirname(__file__)
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
"""
# Пример 5.
"""

iеmport  os

ROOT = os.path.dirname(__file__)   # Путь до папки с программой
dir_name = 'homeworks'             # Создаваемая папкой.
#os.mkdir(os.path.join(ROOT, dir_name))  #Созщдаем директорию
#os.mkdir(dir_name)   #Созщдаем директорию, способ проще.
dir_path = os.path.join(ROOT, dir_name)
if not os.path.exists(dir_name):
    #os.mkdir(dir_path)
    os.makedirs(dir_path)
else:
    #os.rmdir(dir_path)    # Удаляем только пустые папки
    shutil.rmtree(dir_path)   # Удаляем только пустые папки

"""