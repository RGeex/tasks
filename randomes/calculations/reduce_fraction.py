"""
Напишите функцию, которая сводит дроби к их простейшей форме!
Дроби будут представлены в виде массива/кортежа
(в зависимости от языка программирования) исключительно положительных
целых чисел, а сведенная дробь должна быть возвращена в виде массива/кортежа:

input:   [numerator, denominator]
output:  [reduced numerator, reduced denominator]
example: [45, 120] --> [3, 8]
Все числители и знаменатели будут положительными целыми числами.
"""
import unittest
from typing import Any, Callable, Tuple
from fractions import Fraction
from math import gcd


def reduce_fraction(fraction: Tuple[int, int]) -> Tuple[int, int]:
    """
    Приводит дроби к простейшей форме.
    """
    return tuple(i // gcd(*fraction) for i in fraction)


def reduce_fraction_2(fraction: Tuple[int, int]) -> Tuple[int, int]:
    """
    Приводит дроби к простейшей форме.
    """
    tmp = Fraction(*fraction)
    return (tmp.numerator, tmp.denominator)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(reduce_fraction, (
        ((60, 20), (3, 1)),
        ((80, 120), (2, 3)),
        ((4, 2), (2, 1)),
        ((45, 120), (3, 8)),
        ((1000, 1), (1000, 1)),
        ((1, 1), (1, 1)),
    ))
    test(reduce_fraction_2, (
        ((60, 20), (3, 1)),
        ((80, 120), (2, 3)),
        ((4, 2), (2, 1)),
        ((45, 120), (3, 8)),
        ((1000, 1), (1000, 1)),
        ((1, 1), (1, 1)),
    ))
