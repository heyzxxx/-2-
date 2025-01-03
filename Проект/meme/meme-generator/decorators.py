import os

from exceptions import InvalidInputException


def validate_input(func):
    """декоратор для проверки входных данных"""
    def wrapper(*args, **kwargs):
        # проверяем путь к файлу
        for arg in args:
            if isinstance(arg, str) and arg.endswith(".TTF"):
                continue
            elif isinstance(arg, str) and not os.path.exists(arg):
                raise InvalidInputException(f"Путь {arg} недоступен или файл не найден.")
        return func(*args, **kwargs)
    return wrapper
