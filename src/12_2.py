import logging


# named_logger = logging.getLogger("mylogger")
# named_logger.setLevel(logging.WARNING)
#
# named_logger.warning("Я предупреждаю вас")
#
# named_logger.info("FYI")

# # Получаем корневой логер
# logger = logging.getLogger()
#
# # Логируем сообщение уровня ERROR
# logger.error("Это ошибка")
#
# # Получаем логер с определенным именем
# named_logger = logging.getLogger("mylogger")
#
# # Логируем сообщение уровня CRITICAL
# named_logger.critical("Очень критично")

# root_logger = logging.getLogger()
# console_handler = logging.StreamHandler()
# root_logger.addHandler(console_handler)
# root_logger.setLevel(logging.DEBUG)
#
# root_logger.debug("Debug msg")

# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler("src/example.log")
# file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)
#
# logger.debug('Debug message')
# logger.info('Info message')
# logger.warning('Warning message')
# logger.error('Error message')
# logger.critical('Critical message')

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s",
                    filename="application.log",
                    filemode="w",
                    encoding="utf-8")

auth_logger = logging.getLogger("app.auth")
db_logger = logging.getLogger("app.db")
main_logger = logging.getLogger("app.main")

data = {}


def login(username, password):
    auth_logger.info(f'Попытка входа для пользователя: {username}')

    if username == "admin" and password == "qwerty":
        auth_logger.info("Пользователь авторизован")
        return True
    else:
        auth_logger.warning('Неудачная попытка входа')
        return False


def insert(key, value):
    db_logger.info(f"Вставка данных: {key} = {value}")
    data[key] = value


def select(key):
    value = data.get(key)

    if value:
        db_logger.info(f"Получены данные: {key} = {value}")
    else:
        db_logger.warning(f"Данные с ключом {key} не найдены")
    return value


def main():
    try:
        # Записываем сообщение о запуске приложения
        main_logger.info('Запуск приложения')

        # Попытка авторизации
        user_logged_in = login("admin", "qwerty")

        if user_logged_in:
            # Если авторизация успешна, работаем с базой данных
            insert("user_id", "12345")
            select("user_id")
            select(non_existing_id)
        else:
            # Если авторизация не успешна, записываем предупреждение и прекращаем работу
            main_logger.warning("Неудачная авторизация. Прекращение работы")

    except Exception as e:
        # Записываем ошибку, если произошло исключение во время выполнения программы
        main_logger.error(f'Произошла ошибка: {e}', exc_info=True)

    finally:
        # Записываем сообщение о завершении работы приложения
        main_logger.info('Завершение работы приложения')

if __name__ == "__main__":
    main()

