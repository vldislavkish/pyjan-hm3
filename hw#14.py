import random
import re
import string


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
