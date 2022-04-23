"""
Задание 2.3.  * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
Эта задача намного серьёзнее, чем может сначала показаться.
"""

info = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(0, len(info)):
    if info[i].isdigit():
        info.insert(i, '"' + info[i].zfill(2) + '"')
        info.pop(i + 1)
    elif info[i][0:1] == '+':
        info.insert(i, '"+' + info[i][1:].zfill(2) + '"')
        info.pop(i + 1)
    msg = ' '.join(info)
print(info)
print(msg)
