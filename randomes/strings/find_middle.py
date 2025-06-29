"""
Для заданной строки символов создайте функцию, возвращающую среднее число в произведении каждой цифры в строке.

Пример: 's7d8jd9' -> 7, 8, 9 -> 7*8*9=504, таким образом, 0 должен быть возвращен как целое число.

Не все строки будут содержать цифры и не все входные данные будут строкой. В этих случаях верните -1.

Если произведение имеет четное количество цифр, верните средние две цифры.

Пример: 1563 -> 56

ПРИМЕЧАНИЕ: Удалите начальные нули, если произведение четное и первая цифра из двух — ноль. Пример 2016 -> 1
"""
import re
import typing
import unittest
from operator import mul
from functools import reduce


def find_middle(st: typing.Any) -> int:
    """
    Если передана строка, вычисляет среднюю(ние) цифры произведения чисел.
    Если передана не строка возвращает -1.
    """
    if not isinstance(st, str):
        return -1
    num = str(reduce(mul, map(int, re.findall(r'\d', st))))
    a, b = divmod(len(num), 2)
    return int(num[a - int(not b):a + 1])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_middle, (
        ('s7d8jd9', 0),
        ('58jd9fgh/fgh6s.,sdf', 16),
        (None, -1),
        ([1,2,3], -1),
    ))
