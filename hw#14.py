import json
import random
import re
import string
import logging
import xml.etree.ElementTree as xmlET

# Создаем логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создаем обработчик, который выводит лог на консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Создаем форматтер и добавляем его к обработчику
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(console_handler)


class Students:

    @staticmethod
    def make_student_file():
        students = ['sasha', 'tanya', 'masha', 'kirill', 'sergei', 'mihail', 'gleb']
        with open('students.txt', 'w', encoding='UTF-8') as file:
            for _ in range(random.randint(3, 6)):
                gid = ''.join(random.choice(string.hexdigits) for _ in range(12))
                file.write(f'\t\tГруппа {gid}\n')
                file.write('Студент:\tОценка:\n')
                for _ in range(random.randint(3, 7)):
                    file.write(f'\t{random.choice(students)}\t\t\t{random.randint(1, 10)}\n')

    _data: dict[str, dict] = {}

    @classmethod
    def read_student_file(cls):
        with open('students.txt', encoding='UTF-8') as file:
            for line in file:
                lst = line.split()
                if lst[0] == 'Группа':
                    group = lst[1]
                    cls._data.setdefault(group, {'students': [], 'marks': []})
                    continue
                if lst[0] != 'Студент:':
                    cls._data[list(cls._data.keys())[-1]].setdefault('students', ).append(lst[0])
                    cls._data[list(cls._data.keys())[-1]].setdefault('marks', ).append(int(lst[1]))

    @classmethod
    def write_student_file(cls):
        total = 0
        with open('students.txt', 'a', encoding='UTF-8') as file:
            for group in list(cls._data.keys()):
                amount = len(cls._data[group]['students'])
                average_rating = round(sum(cls._data[group]['marks']) / amount, 2)
                file.write(f'В группе {group} {amount} студентов, '
                           f'средняя оценка группы {average_rating}\n')
                total += amount
            file.write(f'Общее кол-во студентов: {total}')


def find_dates(file):
    pat = r"\d{2}\.\d{2}\.[1-9]\d{3}"
    dates = re.findall(pat, file)
    return dates


def is_valid_password(password):
    pat = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{4,}$'
    return bool(re.match(pat, password))


def remove_repeated_words(text):
    corrected_text = re.sub(r'\b(\w+)(\s+\1\b)+', r'\1', text)
    return corrected_text


class UefaJSON:

    @staticmethod
    def write_clubs_uefa_cl():
        data = {
            'Реал Мадрид': {'Страна': 'Испания', 'Трофеев': 15},
            'Милан': {'Страна': 'Италия', 'Трофеев': 7},
            'Бавария': {'Страна': 'Германия', 'Трофеев': 6},
            'Ливерпуль': {'Страна': 'Англия', 'Трофеев': 6},
            'Барселона': {'Страна': 'Испания', 'Трофеев': 5},
            'Аякс': {'Страна': 'Голландия', 'Трофеев': 4},
            'Интернационале': {'Страна': 'Италия', 'Трофеев': 3},
            'Манчестер Юнайтед': {'Страна': 'Англия', 'Трофеев': 3}
        }

        json_data = json.dumps(data)

        with open('uefa.json', 'w', encoding='UTF-8') as file:
            file.write(json_data)

    @staticmethod
    def read_clubs_uefa_cl():
        with open('uefa.json', 'r', encoding='UTF-8') as file:
            dec_data = json.loads(file.read())
            new_dec_data = {k: v['Трофеев'] for k, v in dec_data.items()}
            lst = sorted(new_dec_data.items(), key=lambda item: item[1], reverse=True)
            logger.debug('Клуб с наибольшим количеством побед: %s', lst[0][0])


class GoodsXML:

    @staticmethod
    def make_file_xml():
        root = xmlET.Element('root')

        xmlET.SubElement(root, 'tel1',
                         name='Xiaomi Redmi Note 14 Pro+ 5G 12GB/512GB',
                         price='1490',
                         amount='5')
        xmlET.SubElement(root, 'tel2',
                         name='Apple iPhone 16e 128GB',
                         price='2390',
                         amount='3')
        xmlET.SubElement(root, 'tel3',
                         name='Samsung Galaxy S25 Ultra SM-S938B 12GB/256GB',
                         price='3925',
                         amount='7')

        tree = xmlET.ElementTree(root)
        tree.write('goodsXML.xml')

    @staticmethod
    def read_file_xml():
        with open('goodsXML.xml', encoding='UTF-8') as file:
            root = xmlET.fromstring(file.read())
            logger.debug('Общая стоимость всех товаров: %s',
                         sum(int(tel.attrib['price']) for tel in root))
