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
        for i in range(len(inp)):
            if inp[i] in hidden_number and inp[i] == hidden_number[i]:
                bull += 1
            if inp[i] in hidden_number and inp[i] != hidden_number[i]:
                cow += 1
        if bull != 4:
            print(f'{cow} коровы, {bull} бык')
        else:
            continue
        inp = int(input())
    else:
        print('Вы выиграли!')
