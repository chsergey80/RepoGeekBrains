# 1. Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

def user_words():
    a = 'Exit'
    user_list = []
    while True:
        user_text = input('Введите, пожалуйста, слово : ')
        user_list.append(user_text)
        print(user_list)
        for word in user_list:
            if word == 'stop':
                user_list.remove(user_text)
                return user_list


print(user_words())

#user_words()

#with open('task_5_1.txt', 'w', encoding='utf-8') as f:
    #text = 'Heloo'
    #f.write(text)







