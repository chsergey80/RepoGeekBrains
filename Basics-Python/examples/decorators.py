#Декоратор (англ. Decorator) — структурный шаблон проектирования, предназначенный для динамического подключения
# дополнительного поведения к объекту. Шаблон Декоратор предоставляет гибкую альтернативу практике создания подклассов
# с целью расширения функциональности.

# Пример 1. Регулярные выражения. Пусть есть функция, генерирующая HTML-разметку для тега <input> (без тега <label>
# для упрощения):
#
# def render_input(field):
#     return f'<input id="id_{field}" type="text" name="{field}">'
# username_f = render_input('username')
# print(username_f)

# Предположим, что нам понадобилось обернуть этот тег в другой, например <p> или <li>. Попробуем
# написать функцию-обёртку:

def p_wrapper(func):
    print(func)

    def tag_wrapper(*args, **kwargs):
        print('args', args)
        print('kwargs', kwargs)
        markup = func(*args, **kwargs)
        print(markup)
        return markup
    return tag_wrapper


@p_wrapper    # синтаксически любая функция, написанная с префиксом @ над другой функцией, становится декоратором
def render_input(field):
        return f'<input id="id_{field}" type="text" name="{field}">'


username_f = render_input('username')
print(render_input)


# Пример 2. Декоратор. Маскировка

def simple_cache(func):
    cache = {}
    def wrapper(*args):
        nonlocal cache
        key = str(*args)
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]
    return wrapper

@simple_cache
def render_input(field):
    print(f"call render_input('{field}')")
    return f'<input id="id_{field}" type="text" name="{field}">'


username_f = render_input('username')
password_f = render_input('password')
username_f_2 = render_input('username')
print(username_f)
print(password_f)
print(username_f_2)