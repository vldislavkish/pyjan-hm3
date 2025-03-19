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
