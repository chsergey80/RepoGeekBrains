"""

Задание 5.5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из
трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
#>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

from random import choice


def gen(from_, used_):  # функция считает шутки
    while True:
        n_nouns = choice(from_)
        if not (n_nouns in used_):
            used_.append(n_nouns)
            break

    return (n_nouns, used_)


def get_jokes(count):
    used = []
    answer = []
    for _ in range(count):
        nons, used_ = gen(nouns, used)
        used.append(used_)
        adv, used_ = gen(adverbs, used)
        used.append(used_)
        adj, used_ = gen(adjectives, used)
        used.append(used_)
        answer.append(f"{nons} {adv} {adj}")

    return answer


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(3))