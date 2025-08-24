"""
Дан смешанный массив числовых и строковых представлений целых чисел.
Сложите целые числа, не являющиеся строками, и вычтите сумму строковых
целых чисел.

Вернуть как число.

"""
import typing
import unittest
from operator import sub


def div_con_1(lst: list[int | str]) -> int:
    """
    Вычисляет разницу сумм чисел int и str.
    """
    return sub(*map(sum, zip(*[[0, int(x)][::isinstance(x, str) or -1] for x in lst])))


def div_con_2(lst: list[int | str]) -> int:
    """
    Вычисляет разницу сумм чисел int и str.
    """
    return sum(int(x) * (isinstance(x, int) or -1) for x in lst)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(div_con_1, (
        ([9, 3, '7', '3'], 2),
        (['5', '0', 9, 3, 2, 1, '9', 6, 7], 14),
        (['3', 6, 6, 0, '5', 8, 5, '6', 2, '0'], 13),
        (['1', '5', '8', 8, 9, 9, 2, '3'], 11),
        ([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7], 61),
    ))
    test(div_con_1, (
        ([9, 3, '7', '3'], 2),
        (['5', '0', 9, 3, 2, 1, '9', 6, 7], 14),
        (['3', 6, 6, 0, '5', 8, 5, '6', 2, '0'], 13),
        (['1', '5', '8', 8, 9, 9, 2, '3'], 11),
        ([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7], 61),
    ))
