import random


class Cards:

    @staticmethod
    def list_cards_54():
        inds = ['A'] + [str(_) for _ in range(2, 11)] + [_ for _ in 'JQK']
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
            print({i: v for i, v in enumerate(self.list_cards_54(), start=1)}[num_card])
        elif flag == '+':
            print({i: v for i, v in enumerate(self.shuffle_cards_54(), start=1)}[num_card])

card = Cards
card()
