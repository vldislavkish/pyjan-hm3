from enum import Enum
from datetime import date
import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")


handler = RotatingFileHandler(
    'user_actions.log',
    maxBytes=1024,
    backupCount=7,
    encoding='utf-8'
)
handler.setFormatter(formatter)
logger.addHandler(handler)

stream = logging.StreamHandler()
stream.setFormatter(formatter)
logger.addHandler(stream)


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
            logger.debug('Ошибка')

    @classmethod
    def display_status(cls, order_id: str):
        logger.info('Статус: %s', cls._data[order_id])


def day_difference(first_date: str, second_date: str):
    year, month, day = map(int, first_date.split())
    new_first_date = date(year, month, day)
    year, month, day = map(int, second_date.split())
    new_second_date = date(year, month, day)
    return abs((new_first_date - new_second_date).days)


def past_or_future_date(your_date: str):
    year, month, day = map(int, your_date.split())
    new_your_date = date(year, month, day)
    dif = (date.today() - new_your_date).days
    return 'Будущее' if dif < 0 else 'Прошлое'


def loger_actions():
    try:
        logger.info("Начало программы")

        # Имитация успешного действия
        logger.info("Пользователь открыл файл")

        # Имитация предупреждения
        logger.warning("Пользователь ввёл неверные данные, запрос будет повторён")

        # Имитация ошибки
        raise ValueError("Ошибка чтения файла")
    except Exception as e:
        logger.error("Возникла ошибка: %s", e)
    finally:
        logger.info("Завершение программы")


loger_actions()
