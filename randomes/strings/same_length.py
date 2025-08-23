"""
Ваша задача — реализовать функцию, которая анализирует заданную строку,
состоящую из двоичных цифр (нулей и единиц). Функция должна возвращать
True если:

    За каждой последовательной последовательностью единиц немедленно
    следует такая же последовательность нулей, причем количество единиц
    равно количеству нулей.

    Начальный ноль всегда приводит к False исход.

Вот несколько примеров, иллюстрирующих ожидаемое поведение функции: Примеры

- For the input "110011100010," the function should return True because
every consecutive sequence of ones (e.g., "11," "111," "1") is followed by
an equal-length consecutive sequence of zeroes.

- For the input "101010110," the function should return False because
the sequence of ones ("11") is not followed by an equal-length consecutive
sequence of zeroes.

- "111100001100" # True 

- "111" # False

- "00110100001111 # False, although the number of zeroes and ones is equal,
the consecutive sequence of ones (e.g., "11," "1," "1111") is not followed
by an equal-length consecutive sequence of zeroes.

Примечания

    Входная строка будет содержать только цифры. 0 или 1.
    Длина входной строки ( txt) будет больше нуля.
"""
import typing
import unittest
from itertools import groupby as gb, zip_longest as zl


def same_length(txt: str) -> bool:
    """
    Проверяет соответсвует ли строка заданному шаблону.
    """
    x = [([int(n), 1][i % 2], len(list(x))) for i, (n, x) in enumerate(gb(txt))]
    return not sum(a != b for a, b in zl(x[::2], x[1::2]))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val)
             for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(
        type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(same_length, (
        ('0', False),
        ('10', True),
        ('1010', True),
        ('1001', False),
        ('101', False),
        ('110010', True),
        ('10010', False),
        ('110', False),
        ('11001', False),
        ('1011100010', True),
        ('11100011000', False),
        ('11101010010010', False),
        ('00110100001111', False),
        ('1100111000100', False),
        ('00110011100010', False),
    ))
