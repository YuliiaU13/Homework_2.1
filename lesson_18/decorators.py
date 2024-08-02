"""
Напишіть декоратор, який логує аргументи та результати викликаної функції.
"""

import functools
import logging

logging.basicConfig(
    filename='decorator.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s',
    force=True
)
logger = logging.getLogger("handle_exceptions")


def log_args_and_result(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{fn.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        result = fn(*args, **kwargs)
        print(f"Function '{fn.__name__}' returned: {result}")
        return result

    return wrapper


@log_args_and_result
def add(a, b):
    return a + b


add(3, 4)
add(a=10, b=90)

print('--' * 5)

"""
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""


def handle_exceptions(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(f"Exception occurred in '{function.__name__}' function: {e}")
            logger.info(f"Exception occurred in '{function.__name__}' function: {e}")
            return None
    return wrapper


@handle_exceptions
def divide(a, b):
    return a / b


print(divide(4, 2))
print(divide(4, 0))
print(divide(4, '0'))
print(divide(4, 2, c=2))
