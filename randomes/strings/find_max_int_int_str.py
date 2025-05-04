"""
В этом ката вам будет дана строка, которая содержит строчные буквы и цифры.
Ваша задача — сравнить группы чисел и вернуть наибольшее число.
Числа не будут иметь начальных нулей.

Например, solve("gh12cdy695m1") = 695, потому что это самая большая из всех числовых группировок.
"""
import typing
import unittest
from itertools import groupby


def find_max_int_int_str(st: str) -> int:
    return max(int(''.join(list(b))) for a, b in groupby(st, key=lambda x: x.isdigit()) if a)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_max_int_int_str, (
        ('gh12cdy695m1', 695),
        ('2ti9iei7qhr5', 9),
        ('vih61w8oohj5', 61),
        ('f7g42g16hcu5', 42),
        ('lu1j8qbbb85', 85),
    ))
