import unittest
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


if __name__ == "__main__":
    unittest.main()
