"""
Задание 7.1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

import os

folder_struct = {"my_project": [{"settings": [{"bar": [], "foo": []}], "mainapp": [], "adminapp": [], "authapp": []}]}


def project_starter(pth, struct):
    for fold_node, ch_node in struct.items():
        test_path = os.path.join(pth, fold_node)
        if not os.path.exists(test_path):
            os.mkdir(test_path)
        if len(ch_node) > 0:
            for node in ch_node:
                project_starter(test_path, node)


if __name__ == "__main__":
    project_starter(os.getcwd(), struct=folder_struct)

