# from unittest.mock import patch
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


if __name__ == '__main__':
    unittest.main()
