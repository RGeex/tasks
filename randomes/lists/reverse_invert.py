"""
Перевернуть и инвертировать все целочисленные значения в заданном списке.

[1,12,'a',3.4,87,99.9,-42,50,5.6] --> [-1,-21,-78,24,-5]

Удалить все типы, кроме целых.

"""
import typing
import unittest


def reverse_invert(lst: list[typing.Any]) -> list[int]:
    """
    Инвертирует целые числа в массиве, удаляя все остальные данные.
    """
    return [int(str(abs(x))[::-1]) * (x < 0 or -1) for x in lst if isinstance(x, int)]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(reverse_invert, (
        ([1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]),
        ([-10], [1]),
        ([-9, -18, 99], [9, 81, -99]),
        ([1, 12, 'a', 3.4, 87, 99.9, -42, 50, 5.6], [-1, -21, -78, 24, -5]),
        ([], []),
    ))
