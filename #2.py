def inp_num():
    try:
        num = int(input('Введите число: '))
        return num ** 2
    except ValueError as e:
        return e


def num_even_odd():
    try:
        num = int(input('Введите число: '))
        return 'Чётное' if num % 2 == 0 else 'Нечётное'
    except ValueError as e:
        return e
