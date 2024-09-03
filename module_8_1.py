def add_everything_up(a: int | float | str, b: int | float | str):
    if (isinstance(a, int) or isinstance(a, float) or isinstance(a, str)):
        if (isinstance(b, int) or isinstance(b, float) or isinstance(b, str)):
            try:
                rez = a + b
                # Пусть у float будет 3 знака после запятой
                if isinstance(rez, float):
                    return round(rez, 3)
                return rez

            except TypeError:
                return str(a) + str(b)
    # Любые другие типы
    try:
        return str(a) + str(b)
    except:
        return f'Ошибка - неверный тип данных: {type(a)} и {type(b)}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
