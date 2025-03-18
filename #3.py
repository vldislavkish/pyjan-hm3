def summarisation():
    try:
        num = int(input('Введите число: '))
        return sum(range(1, num + 1))
    except ValueError as e:
        return e
