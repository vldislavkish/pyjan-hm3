import unittest
import io
import sys
from unittest.mock import patch
from bank_library import Bank


class TestRegisterClient(unittest.TestCase):
    @patch('builtins.input', side_effect=["vlad", "petya", "lena"])
    @patch('random.choice', side_effect=lambda seq: seq[0])  # Возвращает всегда первый элемент
    @patch('builtins.print')  # Подменяем print для подавления вывода
    def test_unique_ids(self, _, __, ___):  # Игнорируем неиспользуемые аргументы
        bank = Bank()

        # Регистрируем нескольких клиентов
        bank.register_client()
        bank.register_client()
        bank.register_client()

        # Проверяем уникальность ID
        client_ids = list(bank.show_data().keys())
        self.assertEqual(len(client_ids), len(set(client_ids)))  # Уникальность ID

    @patch('builtins.input', return_value="nik")  # Имитируем ввод имени
    @patch('builtins.print')  # Перехватываем вывод print
    def test_output_matches_storage(self, mock_print, _):
        bank = Bank()

        # Вызываем метод регистрации клиента
        bank.register_client()

        # Получаем клиентский ID из вывода print
        client_id_output = mock_print.call_args[0][0].split()[-1]  # Извлекаем ID из строки вывода

        # Проверяем, что этот ID существует в data
        self.assertIn(client_id_output, bank.show_data())
        # Проверяем, что имя сохранено корректно
        self.assertEqual(bank.show_data()[client_id_output]['name'], "nik")


class TestOpenDepositAccount(unittest.TestCase):
    def setUp(self):
        self.test_data = {'123': {}}

    @patch('builtins.input', side_effect=['123', '1000', '5'])
    def test_valid_input(self, _):
        obj = Bank()
        obj.set_data(self.test_data)
        obj.open_deposit_account()
        self.assertEqual(obj.show_data()['123'], {'start_balance': 1000, 'years': 5})

    @patch('builtins.input', side_effect=['456'])
    def test_invalid_id(self, _):
        obj = Bank()
        obj.set_data(self.test_data)

        # Перенаправляем вывод в StringIO
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Вызываем тестируемую функцию
        obj.open_deposit_account()

        # Возвращаем стандартный вывод
        sys.stdout = sys.__stdout__

        # Проверяем, что вывод содержит сообщение об ошибке
        self.assertIn('Ошибка. Неправильно введён ID', captured_output.getvalue())


class TestCalcDepositInterestRate(unittest.TestCase):
    def setUp(self):
        self.test_data = {'qwe123': {'name': 'qwe', 'start_balance': 1234, 'years': 12}}

    @patch('builtins.input', side_effect=['qwe123'])
    def test_correct_calculation(self, _):
        obj = Bank()
        obj.set_data(self.test_data)

        # Перенаправляем вывод в StringIO
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Вызываем тестируемую функцию
        obj.calc_deposit_interest_rate()

        # Возвращаем стандартный вывод
        sys.stdout = sys.__stdout__

        # Проверяем баланс и разницу
        self.assertIn('2714.8', captured_output.getvalue())
        self.assertIn('1480.8000000000002', captured_output.getvalue())


class TestCloseDeposit(unittest.TestCase):
    def setUp(self):
        self.test_data = {'qwe123': {'name': 'qwe', 'start_balance': 1234, 'years': 12}}

    @patch('builtins.input', side_effect=['qwe123'])
    def test_empty_data(self, _):
        obj = Bank()
        obj.set_data(self.test_data)

        obj.close_deposit()

        self.assertEqual({}, obj.show_data())


if __name__ == "__main__":
    unittest.main()
