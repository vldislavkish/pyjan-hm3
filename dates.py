from datetime import date
from log import logger


def day_difference(fd, sd):
    try:
        fd_object = datetime.strptime(..)
        sd_object = datetime.strptime(..)
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
