import random


class Cards:

    @staticmethod
    def list_cards_54():
        inds = ['A'] + [str(_) for _ in range(2, 11)] + list('JQK')
        masts = 'Clubs ', 'Diamonds ', 'Hearts ', 'Spades '
        jokers = 'Red Joker', 'Black Joker'
        return [mast + ind for mast in masts for ind in inds] + list(jokers)

    @classmethod
    def shuffle_cards_54(cls):
        cards = cls.list_cards_54()
        random.shuffle(cards)
        return cards

    def __init__(self):
        flag = input('Хотите перемешать колоду? (+/-) ')
        num_card = int(input('Выберите карту из колоды в 54 карт: '))
        if flag == '-':
            print(dict(enumerate(self.list_cards_54(), start=1))[num_card])
        elif flag == '+':
            print(dict(enumerate(self.shuffle_cards_54(), start=1))[num_card])


class CurrencyConverter:

    _data = {'BYN': {'USD': 3.2125, 'EUR': 3.489, 'RUB': 0.0357},
             'USD': {'BYN': 3.2125, 'EUR': 0.9208, 'RUB': 89.9155},
             'EUR': {'USD': 1.0861, 'BYN': 3.489, 'RUB': 97.6545},
             'RUB': {'USD': 0.0111, 'BYN': 0.0357, 'EUR': 0.0102}}

    def __init__(self):
        for i, v in enumerate(self._data, start=1):
            print(i, v, sep=': ')

        que1 = int(input('Выберите валюту, которую хотите конвертировать: '))
        amount = float(input('Введите сумму выбранной валюты: '))
        val1 = list(self._data.keys())[que1 - 1]

        for i, v in enumerate(self._data[val1], start=1):
            print(i, v, sep=': ')

        que2 = int(input(f'Выберите заданную валюту: '))
        val2 = list(self._data[val1].keys())[que2 - 1]


        print(f'Из {amount} {val1} получится {round(amount / self._data[val1][val2], 3)} {val2}')


cur = CurrencyConverter
cur()
