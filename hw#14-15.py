import random
import string


class Students:

    @staticmethod
    def make_student_file():
        students = ['sasha', 'tanya', 'masha', 'kirill', 'sergei', 'mihail', 'gleb']
        file = open('students.txt', 'w', encoding='UTF-8')
        for _ in range(random.randint(3, 6)):
            file.write(f'\t\tГруппа {''.join(random.choice(string.hexdigits) 
                                             for _ in range(12))}\n')
            file.write('Студент:\tОценка:\n')
            for _ in range(random.randint(3, 7)):
                file.write(f'\t{random.choice(students)}\t\t\t{random.randint(1, 10)}\n')
        file.close()

    _data: dict[str, dict] = {}

    @classmethod
    def read_student_file(cls):
        file = open('students.txt', encoding='UTF-8')
        for line in file:
            lst = line.split()
            if lst[0] == 'Группа':
                group = lst[1]
                cls._data.setdefault(group, {'students': [], 'marks': []})
                continue
            if lst[0] != 'Студент:':
                cls._data[list(cls._data.keys())[-1]].setdefault('students', ).append(lst[0])
                cls._data[list(cls._data.keys())[-1]].setdefault('marks', ).append(int(lst[1]))
        file.close()

    @classmethod
    def write_student_file(cls):
        total = 0
        file = open('students.txt', 'a', encoding='UTF-8')
        for group in list(cls._data.keys()):
            amount = len(cls._data[group]['students'])
            average_rating = round(sum(cls._data[group]['marks']) / amount, 2)
            file.write(f'В группе {group} {amount} студентов, '
                       f'средняя оценка группы {average_rating}\n')
            total += amount
        file.write(f'Общее кол-во студентов: {total}')
        file.close()
