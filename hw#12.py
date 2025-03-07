import random
import string


class Bank:
    _data: dict[str, dict] = {}

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


class Library:
    _data_books: dict[str, dict] = {}
    _data_readers: dict[str, dict] = {}

    def adding_book(self, author, book_name, num_pages, isbn, reserved=False):
        if author not in self._data_books:
            self._data_books.setdefault(author, {isbn: [book_name, num_pages, reserved]})
        else:
            self._data_books[author].setdefault(isbn, [book_name, num_pages, reserved])

    def adding_reader(self):
        client_id = ''.join(random.choice(string.hexdigits) for _ in range(12))
        self._data_readers.setdefault(client_id, {})
        print(f'Ваш ID: {client_id}')

    def reserve_book(self):
        r_id = input('Введите ваш ID: ')
        if r_id in self._data_readers:
            for author in self._data_books:
                print(f'Автор: {author}')
                for isbn, prod in self._data_books[author].items():
                    print(f'\tНазвание книги: {prod[0]}, кол-во страниц: {prod[1]}, ISBN: {isbn} {'зарезервирована' if prod[2] else ''}')
            print()
            wyw = input('Введите ISBN книги, которую хотите зарезервировать: ')
            for author in self._data_books:
                if wyw in self._data_books[author]:
                    if self._data_books[author][wyw][-1]:
                        print('К сожалению книга зарезервирована, попробуйте другую')
                    else:
                        self._data_books[author][wyw][-1] = True
                        self._data_readers[r_id].setdefault(wyw, self._data_books[author][wyw])
                        print('Книга успешно зарезервирована')
        else:
            print('Неверный ID')




lib = Library()
lib.adding_book('Tolkien', 'Hobbit', 400, '000465189')
lib.adding_book('Tolkien', 'Rabbit', 123, '000498789489')
lib.adding_book('Tolstoy', 'Mir i mir', 13, '123123123213')
lib.adding_reader()
lib.reserve_book()
lib.reserve_book()
print(lib._data_books)
print(lib._data_readers)
