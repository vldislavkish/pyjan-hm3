from enum import Enum
from log import logger


class OrderStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    READY = 3
    COMPLETED = 4
    CANCELLED = 5


class Order:
    _OrderStatus = iter(OrderStatus)
    _data: dict[str, OrderStatus] = {}

    def __init__(self, order_id: str):
        self.order_id = order_id
        self._data.setdefault(order_id, next(self._OrderStatus))

    @classmethod
    def update_status(cls, order_id: str):
        if order_id in cls._data:
            try:
                cls._data[order_id] = next(cls._OrderStatus)
            except StopIteration:
                # Если достигнут конец последовательности статусов
                logger.warning('Статус для заказа %s уже на последнем этапе.',
                               order_id)
        else:
            logger.debug('Ошибка: заказ не найден.')

    @classmethod
    def display_status(cls, order_id: str):
        if order_id in cls._data:
            logger.info('Статус заказа %s: %s',
                        order_id, cls._data[order_id].name)
        else:
            logger.error('Заказ с ID %s не найден.', order_id)
