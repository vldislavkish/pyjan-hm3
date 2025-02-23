import random


def filter_lst(lst: list) -> list:
    exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return sorted(set(lst) - set(exclude), key=lambda x: x[0])


def is_palindrom(stroka: str) -> bool:
    return stroka == stroka[::-1]


def calculate_salary(salary: int, bonus=True) -> str:
    if bonus:
        salary *= 10
    return f'${salary}'


def count_vowls(word):
    vowls = 'aeiouyAEIOUY'
    count = 0
    for w in word:
        if w in vowls:
            count += 1
    return count


def sort_vowel(lst: list[str]):
    return sorted(lst, key=count_vowls)


def generate_password(n: int) -> str:
    if n < 4:
        raise ValueError('Пароль должен содержать минимум 4 символа')
    lst_pass = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                'abcdefghijklmnopqrstuvwxyz',
                '1234567890',
                r'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~']
    password = [random.choice(l) for l in lst_pass]
    while len(password) != n:
        ind = random.randint(0, 3)
        password.append(random.choice(lst_pass[ind]))
    return ''.join(password)


def calculate_sum(numbers: list[int]) -> int:
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 0:
        return 0
    numbers[0] += numbers.pop()
    if len(numbers) != 1:
        calculate_sum(numbers)
    return numbers[0]


def double_elements(numbers: list[int]) -> list[int]:
    return list(map(lambda x: x * 2, numbers))


def filter_even_numbers(numbers: list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == 0, numbers))
