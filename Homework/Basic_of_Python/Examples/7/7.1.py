def get_sales(f_name):
    with open(f_name, 'r', encoding='utf-8') as f:
        return f.read().splitlines()  # считаем, что файл небольшой и поместится в оперативную память


def parse_sales(sales):
    return [
        float(el.strip().replace(',', '.'))
        for el in sales
    ]


def aggregate(sales):
    return {
        'sum': sum(sales)
    }


def sales_validator(sales):
    '''проверяет на наличие чисел меньше 1000'''
    for el in sales:
        if el < 1000:
            raise ValueError(f'too low price: {el}')
    return sales


if __name__ == '__main__':
    import sys

    try:
        _sales = get_sales('bakery.csv')  # в одном блоке код с разными исключениями, можно несколько try-except
        sales = parse_sales(_sales)
        sales = sales_validator(sales)
    except (ValueError, TypeError) as e:
        print(f'wrong value: {e.args[0]}')
        sys.exit(2)
    except FileNotFoundError as e:
        print(f'error: {e}')
        raise e  # пробрасывание исключения
    except Exception as e:  # ловит все исключения, идёт последним
        print(e, file=sys.stderr)
        sys.exit(1)
    else:  # если исключений не было
        summary = aggregate(sales)  # тут не должно быть исключений, не пишем в try-except
        print(summary)
    finally:  # выполняется в конце в любом случае
        print(sales)
