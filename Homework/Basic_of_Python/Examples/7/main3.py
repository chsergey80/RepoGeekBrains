import os
import shutil

ROOT = os.path.dirname(__file__)
dir_name = 'homeworks/lesson1'
#os.mkdir(os.path.join(ROOT, dir_name))
dir_path = os.path.join(ROOT, dir_name)
if not os.path.exists(dir_path):
    #os.mkdir(dir_path)
    os.makedirs(dir_path)
else:
    #os.rmdir(dir_path)  # только пустые папки удаляет
    shutil.rmtree(dir_path)