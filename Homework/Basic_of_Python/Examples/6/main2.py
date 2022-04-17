# with open('file2.dat', 'w', encoding='utf-8') as f:
#with open('file2.dat', 'x', encoding='utf-8') as f:
with open('file2.dat', 'a+', encoding='utf-8') as f:
    # f.write('Привет\n')
    # f.writelines(['Python ', '3\n'])
    # print('More Python!', file=f)
    # print('More Python!', file=f)
    print(f.tell())
    f.seek(0)
    print(f.tell())
    content = f.read()
    print(content)