import unittest
from unittest.mock import patch
from bank_library import Bank


class TestRegisterClient(unittest.TestCase):
    @patch('builtins.input', side_effect=["vlad", "petya", "lena"])
    @patch('random.choice', side_effect=lambda seq: seq[0])  # Возвращает всегда первый элемент
    @patch('builtins.print')  # Подменяем print для подавления вывода
    def test_unique_ids(self, _, __, ___): # игнорируем неиспользуемые аргументы
        bank = Bank()

        # Регистрируем нескольких клиентов
        bank.register_client()
        bank.register_client()
        bank.register_client()

        # Проверяем уникальность ID
        client_ids = list(bank.show_data().keys())
        self.assertEqual(len(client_ids), len(set(client_ids)))  # Уникальность ID


if __name__ == "__main__":
    unittest.main()
