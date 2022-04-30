# https://pythonworld.ru/osnovy/dekoratory.html
def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():  # принимает аргументы
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()  # Сама функция
        print("А я - код, срабатывающий после")

    # Вернём эту функцию
    return the_wrapper_around_the_original_function


def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")


@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")


stand_alone_function()
print()

# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# готовую к использованию функцию:
stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()
print()

another_stand_alone_function()
