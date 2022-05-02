"""
Задание 7.5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в
котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""

import os


size = {}

def scan_mem(pth):
    if not os.path.exists(pth):
        return
    with os.scandir(pth) as files:
        for node in files:
            if node.is_file():
                mem = 10 ** len(str(os.stat(node).st_size))
                file_extend = os.path.splitext(node)[-1]
                count, extends = size.get(mem, (0, set()))
                extends.add(file_extend)
                count += 1
                size[mem] = (count, extends)
            elif node.is_dir():
                scan_mem(os.path.join(pth, node))


if __name__ == "__main__":
    pth = os.getcwd()
    scan_mem(pth)
    print({ k:(size[k][0], list(size[k][1])) for k in size})