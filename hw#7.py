import random


def bulls_and_cows():
    digits = list(range(10))
    random.shuffle(digits)
    while digits[0] == 0:
        random.shuffle(digits)
    hidden_number = digits[:4]
    print(*hidden_number, sep='')
    inp = int(input())
    while inp != hidden_number:
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
            break
        inp = int(input())
    print('Вы выиграли!')


def pyramid(n: int) -> None:
    for i in range(n):
        print(' ' * (n - i) + '*' * (i + 1), end='')
        print('*' * i)


def statues(inp):
    stat = set(map(int, inp.split()))
    rng = set(range(min(stat), max(stat)))
    print(rng - stat)

statues('0 2 5 3 11')
