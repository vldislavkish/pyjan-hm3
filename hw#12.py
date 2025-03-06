import random
import string


class Bank:
    _data = {}

    def register_client(self):
        name = input('Введите свое имя: ')
        client_id = ''.join(random.choice(string.hexdigits) for _ in range(12))
        print(f'Ваш ID: {client_id}')
        self._data.setdefault(client_id, {'name': name})

    def open_deposit_account(self):
        client_id = input('Введите Ваш ID: ')
        if client_id in self._data:
            start_balance = int(input('Введите Ваш вклад: '))
            years = int(input('Введите срок (лет): '))
            self._data.setdefault(client_id, {}).update(start_balance=start_balance, years=years)
        else:
            print('Ошибка. Неправильно введён ID')

    def calc_deposit_interest_rate(self):
        client_id = input('Введите Ваш ID: ')
        if client_id in self._data and len(self._data.get(client_id)) > 1:
            month = self._data.get(client_id).get('years') * 12
            balance = self._data.get(client_id).get('start_balance')
            procent = 10 / 12 / 100
            dep = tuple(balance + (balance * procent * (i + 1)) for i in range(month))
            print(f'За {month} месяцев на Вашем балансе будет {dep[-1]} под 10% годовых,'
                  f' разница: {dep[-1] - balance}')
        else:
            print('Ошибка. Неправильно введён ID или не открыт депозит')

    def close_deposit(self):
        client_id = input('Введите Ваш ID: ')
        if client_id in self._data:
            del self._data[client_id]
        else:
            print('Ошибка. Неправильно введён ID')


bank = Bank()
bank.register_client()
bank.open_deposit_account()
bank.calc_deposit_interest_rate()
bank.close_deposit()
