def ex1():
    #Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
    print('www.my_site.com#about'.replace('#', '/'))


def ex2():
    #Напишите программу, которая добавляет ‘ing’ к словам
    print(input('Введите слово, к которому хотите добавить "ing" в конце: ') + 'ing')


def ex3():
    #В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
    print(' '.join('Ivanou Ivan'.split()[::-1]))


def ex4():
    #Напишите программу, которая удаляет пробел в начале, в конце строки
    print(input('Введите слово, в котором хотите удалить пробелы в начале и в конце строки: ').strip())


def ex5():
    #Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
    #Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению.
    print(input('Слово с заглавной буквы').title())


def ex6():
    #Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
    print('Robin Singh'.split())


def ex7():
    #"I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
    print('I love arrays they are my favorite'.split())


def ex8():
    #Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus.Напечатайте текст:
    # “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
    lst = ['Ivan', 'Ivanou']
    town, city = 'Minsk', 'Belarus'
    print(f'Привет, {' '.join(lst)}! Добро пожаловать в {town} {city}')


def ex9():
    #Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
    #сделайте из него строку => "I love arrays they are my favorite"
    lst = ["I", "love", "arrays", "they", "are", "my", "favorite"]
    print(' '.join(lst))


def ex10():
    #Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
    import random
    import string
    lst = [random.choice(string.printable) for _ in range(10)]
    print(lst)
    lst[2] = 'новое значение'
    print(lst)
    del lst[6]
    print(lst)