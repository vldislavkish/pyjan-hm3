import random
import re


def bulls_and_cows():
    digits = list(range(10))
    random.shuffle(digits)
    while digits[0] == 0:
        random.shuffle(digits)
    hidden_number = digits[:4]
    print('Загаданное число: ', end='')
    print(*hidden_number, sep='')

    while True:
        inp = input('Введите 4-значное число с неповторяющимися цифрам,не начинающееся на 0: ')
        if not bool(re.fullmatch(r"[1-9]\d\d\d", inp)) or len(set(inp)) != len(inp):
            print('Ошибка ввода.')
            continue
        inp = [int(d) for d in str(inp)]
        bull, cow = 0, 0
        for i, v in enumerate(inp):
            if v in hidden_number and v == hidden_number[i]:
                bull += 1
            if v in hidden_number and v != hidden_number[i]:
                cow += 1
        if bull != 4:
            print(f'{cow} коровы, {bull} бык')
        else:
            print('Вы выиграли!')
            break


def pyramid(n: int) -> None:
    for i in range(n):
        print(' ' * (n - i) + '*' * (i + 1), end='')
        print('*' * i)


def statues(inp: list) -> None:
    if not all(isinstance(i, int) for i in inp):
        raise ValueError("Все элементы списка должны быть числами.")
    stat = set(inp)
    rng = set(range(min(stat), max(stat)))
    print(len(rng - stat))
