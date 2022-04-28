import os

# files = os.listdir()
# print(files)
# for file in files:
#     print(os.path.isdir(file))
#     print(os.path.isfile(file))
#     print(os.stat(file).st_size)

root_dir = './'
# for item in os.scandir(root_dir):
#     #print(type(item))
#     print(item.is_dir())
#     print(item.is_file())
#     print(item.stat().st_size)

for root, dirs, files in os.walk(root_dir):
    # print(root)
    # print(dirs)
    # print(files)
    # print(type(root))
    for file in files:
        #print(f'{root}/{file}')  # не кроссплатформенно
        f_path = os.path.join(root, file)  # кроссплатформенно
        #print(f_path)
        #print(os.path.abspath(f_path))
        print(os.path.exists(f_path))
        print(os.stat(f_path).st_size)
        print(os.path.split(f_path))
        print(os.path.dirname(f_path), os.path.basename(f_path))