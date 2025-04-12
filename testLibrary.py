from unittest.mock import patch
import unittest
import io
import sys
from bank_library import Library  # Предположим, что ваш класс находится в файле library.py


class TestAddingBook(unittest.TestCase):
    def setUp(self):
        self.obj = Library()
        self.obj.red_data_books({('qwe', 'asd', '123', '12aw21'): [False, False]})

    def test_negative_result(self):
        # Перенаправляем вывод в StringIO
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Выполняем метод
        self.obj.adding_book('qwe', 'asd', '123', '12aw21')

        # Возвращаем стандартный вывод
        sys.stdout = sys.__stdout__

        # Проверяем отрицательный результат
        self.assertIn('Данная книга есть в наличии', captured_output.getvalue())


class TestAddingReader(unittest.TestCase):
    def setUp(self):
        self.obj = Library()

    def test_adding_reader(self):
        # Перенаправляем вывод в StringIO для проверки вывода
        captured_output = io.StringIO()
        sys.stdout = captured_output

        self.obj.adding_reader()

        # Захватываем вывод client_id из метода
        output = captured_output.getvalue().strip()

        # Проверяем, что client_id сгенерирован
        self.assertTrue(output.startswith('Ваш ID: '))

        # Извлекаем сгенерированный client_id из вывода
        client_id = output.split(': ')[1]

        # Проверяем, что client_id есть в _data_readers
        self.assertIn(client_id, self.obj.return_data_readers())

        # Проверяем, что у нового пользователя списки пустые
        self.assertEqual(self.obj.return_data_readers()[client_id], {'reserved': [], 'taken': []})


class TestReserveBook(unittest.TestCase):
    def setUp(self):
        self.obj = Library()
        self.obj.red_data_books({('qwe', 'asd', '123', '12aw21'): [False, False]})
        self.obj.red_data_readers({'id123': {'reserved': [], 'taken': []}})

    @patch('builtins.input', side_effect=['id123', '12aw21'])
    @patch('builtins.print')
    def test_reserve_book(self, _, __):

        self.obj.reserve_book()
        # Проверяем, что книга зарезервирована (флаг изменился на True)
        self.assertTrue(list(self.obj.return_data_books().values())[0][0])
        # Проверяем, что книга зарезервирована за пользователем
        self.assertEqual(tuple(self.obj.return_data_readers().values())[0]['reserved'][0],
                         ('qwe', 'asd', '123', '12aw21'))


class TestReserveBookBeingRead(unittest.TestCase):
    def setUp(self):
        self.obj = Library()
        self.obj.red_data_books({('qwe', 'asd', '123', 'q1'): [False, True]})
        self.obj.red_data_readers({'8b3': {'reserved': [], 'taken': [('qwe', 'asd', '123', 'q1')]},
                                   'b2d': {'reserved': [], 'taken': []}})

    @patch('builtins.input', side_effect=['b2d', 'q1'])
    @patch('builtins.print')
    def test_reserve_book_being_read(self, _, __):

        self.obj.reserve_book()
        # Проверяем, что книга зарезервирована за пользователем
        # и по-прежнему взята другим пользователем
        self.assertTrue(self.obj.return_data_readers()['b2d']['reserved'][0])
        self.assertEqual(self.obj.return_data_readers()['8b3']['taken'][0],
                         ('qwe', 'asd', '123', 'q1'))

        # Проверяем, что книга взята и зарезервирована
        self.assertEqual(sum(self.obj.return_data_books()[('qwe', 'asd', '123', 'q1')]), 2)


if __name__ == '__main__':
    unittest.main()
