"""
Ваша задача — создать функцию, которая принимает в качестве аргумента любое неотрицательное целое
число и возвращает его вместе с цифрами в порядке убывания. По сути, нужно переставить цифры,
чтобы получить максимально возможное число.

Примеры:
Вход: 42145 Выход:54421

Вход: 145263 Выход:654321

Вход: 123456789 Выход:987654321
"""
import unittest
from typing import Any, Callable, Tuple


def descending_order(num: int) -> int:
    """
    Из переданного числа создает максимальное.
    """
    return int(''.join(sorted(str(num), reverse=True)))


def descending_order_2(num: int) -> int:
    """
    Из переданного числа создает максимальное.
    """
    return int(''.join(sorted(str(num))[::-1]))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(descending_order, (
        (0, 0),
        (15, 51),
        (123456789, 987654321),
    ))
    test(descending_order_2, (
        (0, 0),
        (15, 51),
        (123456789, 987654321),
    ))
