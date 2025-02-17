"""
Найдите номер с наибольшим количеством цифр.
Если два числа в массиве аргументов имеют одинаковое количество цифр, верните первое в массиве.
"""
import typing
import unittest


def find_longest(arr: list[int]) -> int:
    """
    Поиск максимального по длинее числа в списке.
    """
    return max(arr, key=lambda x: len(str(x)))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_longest, (
        ([1, 10, 100], 100),
        ([9000, 8, 800], 9000),
        ([8, 900, 500], 900),
        ([3, 40000, 100], 40000),
        ([1, 200, 100000], 100000),
    ))
