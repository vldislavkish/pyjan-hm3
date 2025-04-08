# from unittest.mock import patch
import unittest
import io
import sys
from bank_library import Library  # Предположим, что ваш класс находится в файле library.py


class TestAddingBook(unittest.TestCase):
    def setUp(self):
        self.obj = Library()
        self.obj.return_data_books({('qwe', 'asd', '123', '12aw21'): [False, False]})

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
