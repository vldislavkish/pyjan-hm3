import random
import string


class Bank:
    __data: dict[str, dict] = {}

    def show_data(self):
        return self.__data

    def set_data(self, new_data):
        self.__data = new_data

    def register_client(self):
        name = input('Введите свое имя: ')
        client_id = ''.join(random.choice(string.hexdigits) for _ in range(12))
        print(f'Ваш ID: {client_id}')
        self.__data.setdefault(client_id, {'name': name})

    def open_deposit_account(self):
        client_id = input('Введите Ваш ID: ')
        if client_id in self.__data:
            start_balance = int(input('Введите Ваш вклад: '))
            years = int(input('Введите срок (лет): '))
            self.__data.setdefault(client_id, {}).update(start_balance=start_balance, years=years)
        else:
            print('Ошибка. Неправильно введён ID')

    def calc_deposit_interest_rate(self):
        client_id = input('Введите Ваш ID: ')
        if client_id in self.__data and len(self.__data.get(client_id)) > 1:
            month = self.__data.get(client_id).get('years') * 12
            balance = self.__data.get(client_id).get('start_balance')
            procent = 10 / 12 / 100
            dep = tuple(balance + (balance * procent * (i + 1)) for i in range(month))
            print(f'За {month} месяцев на Вашем балансе будет {dep[-1]} под 10% годовых,'
                  f' разница: {dep[-1] - balance}')
        else:
            print('Ошибка. Неправильно введён ID или не открыт депозит')

    def close_deposit(self):
        client_id = input('Введите Ваш ID: ')
        if client_id in self.__data:
            del self.__data[client_id]
        else:
            print('Ошибка. Неправильно введён ID')


class Library:
    _data_books: dict[tuple, list] = {}
    _data_readers: dict[str, dict] = {}

    def red_data_books(self, red_data_books):
        self._data_books = red_data_books

    def red_data_readers(self, red_data_readers):
        self._data_readers = red_data_readers

    def return_data_books(self):
        return self._data_books

    def return_data_readers(self):
        return self._data_readers

    def show_list_books(self):
        for author, book_name, num_pages, isbn in self._data_books:
            reserved = 'ЗАРЕЗЕРВИРОВАНА' \
                if self._data_books[author, book_name, num_pages, isbn][0] else ''
            taken = 'ИСПОЛЬЗУЕТСЯ' \
                if self._data_books[author, book_name, num_pages, isbn][1] else ''
            print(f'Автор: {author}, '
                  f'название: {book_name}, '
                  f'кол-во страниц: {num_pages}, '
                  f'ISBN: {isbn}', end=' ')
            print(f'{reserved} {taken}')

    def adding_book(self, author, book_name, num_pages, isbn):
        if (author, book_name, num_pages, isbn) not in self._data_books:
            self._data_books.setdefault((author, book_name, num_pages, isbn), [False, False])
        else:
            print('Данная книга есть в наличии')

    def adding_reader(self):
        client_id = ''.join(random.choice(string.hexdigits) for _ in range(12))
        self._data_readers.setdefault(client_id, {'reserved': [], 'taken': []})
        print(f'Ваш ID: {client_id}')

    def reserve_book(self):
        r_id = input('Введите ваш ID: ')
        if r_id in self._data_readers:
            self.show_list_books()
            wyw = input('Введите ISBN книги, которую хотите зарезервировать: ')
            for author, rvd_tkn in self._data_books.items():
                if wyw in author:
                    if rvd_tkn[0]:
                        print('К сожалению книга зарезервирована, попробуйте другую')
                    else:
                        rvd_tkn[0] = True
                        self._data_readers[r_id]['reserved'].append(author)
                        print('Книга успешно зарезервирована')
        else:
            print('Неверный ID')

    def cancel_reserve(self):
        r_id = input('Введите ваш ID: ')
        if r_id in self._data_readers:
            wyw = input('Введите ISBN книги, для которой хотите отклонить резервацию: ')
            for i, v in enumerate(self._data_readers[r_id]['reserved']):
                if wyw in v:
                    del self._data_readers[r_id]['reserved'][i]
                    for author, rvd_tkn in self._data_books.items():
                        if wyw in author:
                            rvd_tkn[0] = False
                            print('Резервация отклонена')
                            break
            print('Вы не резервировали данну книгу')
        else:
            print('Неверный ID')

    def get_book(self):
        r_id = input('Введите ваш ID: ')
        if r_id in self._data_readers:
            self.show_list_books()
            wyw = input('Введите ISBN книги, которую хотите взять: ')
            for book, rvd_tkn in self._data_books.items():
                if wyw in book:
                    if rvd_tkn[0]:
                        if rvd_tkn[1]:
                            print('К сожалению книга используется, попробуйте другую')
                            break
                        if book in self._data_readers[r_id]['reserved']:
                            rvd_tkn[1] = True
                            self._data_readers[r_id]['taken'].append(book)
                            print('Книга успешно взята')
                            rvd_tkn[0] = False
                            ind = self._data_readers[r_id]['reserved'].index(book)
                            del self._data_readers[r_id]['reserved'][ind]
                        else:
                            print('К сожалению книга зарезервирована, попробуйте другую')
                    else:
                        rvd_tkn[1] = True
                        self._data_readers[r_id]['taken'].append(book)
                        print('Книга успешно взята')
                        if rvd_tkn[0]:
                            rvd_tkn[0] = False
        else:
            print('Неверный ID')

    def return_book(self):
        r_id = input('Введите ваш ID: ')
        if r_id in self._data_readers:
            wyw = input('Введите ISBN книги, которую хотите вернуть: ')
            for i, v in enumerate(self._data_readers[r_id]['taken']):
                if wyw in v:
                    del self._data_readers[r_id]['taken'][i]
                    for author, rvd_tkn in self._data_books.items():
                        if wyw in author:
                            rvd_tkn[1] = False
                            print('Спасибо, что вернули книгу')
                            break
                print('Вы не брали такую книгу')
        else:
            print('Неверный ID')
