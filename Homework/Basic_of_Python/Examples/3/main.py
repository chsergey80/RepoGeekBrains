#def show_prices(*args, show_delim=True):  # обязательные и необязательные (по умолчанию)
def show_prices(*args, **kwargs):
    print(args)
    print(kwargs)
    for price in args:
        price = int(round(price * 100))
        rubles = price // 100
        cents = price % 100
        print(f'{rubles:02d} руб {cents:02d} коп', end=', ')
    # if show_delim:
    #     print('*' * 25)


#prices = [57.8, 46.51, 97, 56.78, 89.76, 32.45, 12.78, 83.84, 26.89, 67.87, 34.68, 23.45, 34.6]
# prices = [57.8, 46.51, 97, 56.78, 89.76, 32.45, 12.78, 83.84, 26.89, 67.87
# show_prices(prices)
show_prices(57.8, 46.51, 97, 56.78, 89.76, 32.45, 12.78, h=83.84, g=26.89, k=67.87)
# prices.sort()
# show_prices(prices)
# prices_desc = sorted(prices, reverse=True)
# show_prices(prices_desc)
# show_prices(prices_desc[4::-1], False)  # позиционные
# show_prices(show_delim=False, items=prices_desc[4::-1])  # именованные
# print(show_prices(prices))
