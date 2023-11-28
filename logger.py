import logging

# Создаем объект логгера
logger = logging.getLogger("calculator_logger")
logger.setLevel(logging.DEBUG)

# Создаем обработчик для записи в файл
file_handler = logging.FileHandler("calculator.log")
file_handler.setLevel(logging.INFO)

# Создаем форматтер для форматирования записей лога
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)
