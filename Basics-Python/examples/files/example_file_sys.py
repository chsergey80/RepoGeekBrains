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
import os

root = r'C:\Python3.8\Lib\site-packages\django'
folder = r'C:\Python3.8\Lib\site-packages\django\contrib\admin'
django_admin_dirs = [
os.path.relpath(item, root)
for item in os.scandir(folder)
if item.is_dir() and not item.name.startswith('_')
]
print(django_admin_dirs)
# Пример 10.
"""
import os

files = os.listdir()
print(files)
for file in files:
    print(os.path.isdir(file))
    print(os.path.isfile(file))
    print(os.stat(file).st_size)
"""
# Пример 2.
import shutil

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