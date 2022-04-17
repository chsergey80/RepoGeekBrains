# f_name = r'C:\file.dat'
# f_name = 'C:\\file.dat'
# f_name = 'C:/Program files/file.dat'
f_name = 'file.dat'
# f = open(f_name, 'r', encoding='utf-8')
# with open(f_name, 'r', encoding='utf-8') as f1, \
#         open(f_name, 'r', encoding='utf-8') as f2:
with open(f_name, 'r', encoding='utf-8') as f:
    f.seek(45)
    print(f.read())
    # with open(f_name, 'r', encoding='utf-8') as f2:
    #     #content = f.read(6)
    #     # #rows = content.split('\n')
    #     # rows = content.splitlines()  # кроссплатформенное
    #     #rows = f.readlines(6)
    #     rows = f2.readline(3)
    #     #print(content)
    #     print(rows)
# for row in f:
#     print(row, end='')
# while True:
#     row = f.readline()
#     print(row, end='')
#     if not row:
#         break


#print(type(f))
#print(f)
#print(dir(f))
# print(f.closed)
# f.close()
# print(f.closed)
