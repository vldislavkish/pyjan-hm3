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


def day_difference():
    fd, sd = (input('Введите дату в формате "year.month.day"\nПервая дата: '),
              input('Вторая дата: '))
    try:
        year, month, day = map(int, fd.split('.'))
        n_fd = date(year, month, day)
        year, month, day = map(int, sd.split('.'))
        n_sd = date(year, month, day)
        return abs((n_fd - n_sd).days)
    except ValueError as e:
        logger.warning('Неправильно указана дата')
        return e


def past_or_future_date():
    yd = input('Введите дату в формате "year.month.day"\nВаша дата: ')

    try:
        year, month, day = map(int, yd.split('.'))
        n_yd = date(year, month, day)
        dif = (date.today() - n_yd).days
        return 'Будущее' if dif < 0 else 'Прошлое'
    except ValueError as e:
        logger.warning('Неправильно указана дата')
        return e


def loger_actions():
    try:
        logger.info("Начало программы")

        # Имитация успешного действия
        logger.info("Пользователь открыл файл")

        # Имитация предупреждения
        logger.warning("Пользователь ввёл неверные данные, "
                       "запрос будет повторён")

        # Имитация ошибки
        raise ValueError("Ошибка чтения файла")
    except ValueError as e:
        logger.error("Возникла ошибка: %s", e)
    except FileNotFoundError as e:
        logger.error("Файл не найден: %s", e)
    finally:
        logger.info("Завершение программы")
