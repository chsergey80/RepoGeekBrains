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