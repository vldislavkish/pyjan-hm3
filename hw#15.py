from enum import Enum
from datetime import date


class Order:
    _OrderStatus = iter(Enum(
        'OrderStatus', 'PENDING '
                        'IN_PROGRESS '
                        'READY '
                        'COMPLETED '
                        'CANCELLED ', start=1))
    _data = {}

    def __init__(self, order_id: str):
        self.order_id = order_id
        self._data.setdefault(order_id, next(self._OrderStatus))

    @classmethod
    def update_status(cls, order_id: str):
        if order_id in cls._data:
            cls._data[order_id] = next(cls._OrderStatus)
        else:
            print('Ошибка')

    @classmethod
    def display_status(cls, order_id: str):
        print(cls._data[order_id])


def day_difference(first_date: str, second_date: str):
    year, month, day = map(int, first_date.split())
    new_first_date = date(year, month, day)
    year, month, day = map(int, second_date.split())
    new_second_date = date(year, month, day)
    return abs((new_first_date - new_second_date).days)

