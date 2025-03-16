from enum import Enum


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
