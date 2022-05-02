"""
Задание 7.3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
например, во фреймворке django.
"""

import os
import shutil


glb_path = os.getcwd()
files = [os.path.relpath(os.path.join(root, file), glb_path) for root, _, files in os.walk(
    glb_path) for file in files if file.endswith(".html")]
for rel_path in files:
    path, file = os.path.split(rel_path)
    test_path = os.path.join(glb_path, "template", path)
    if not os.path.exists(test_path):
        os.makedirs(test_path)
    shutil.copyfile(os.path.join(glb_path,rel_path), os.path.join(test_path, file))
