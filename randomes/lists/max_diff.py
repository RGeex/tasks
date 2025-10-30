"""
Вам необходимо реализовать функцию, которая возвращает разницу между
наибольшим и наименьшим значением в заданном диапазоне. list / array( lst)
получен в качестве параметра.

lstсодержит целые числа, это значит, что он может содержать некоторые
отрицательные числа
если lstпусто или содержит один элемент, вернуть 0
lstне отсортировано
[1, 2, 3, 4]   //  returns 3 because 4 -   1  == 3
[1, 2, 3, -4]  //  returns 7 because 3 - (-4) == 7
"""
import typing
import unittest
from operator import sub


def max_diff(lst: list[int]) -> int:
    """
    Определяет разницу между максимальным и минимальным значениями списка.
    """
    return len(lst) > 1 and sub(*sorted(lst)[-1::-len(lst) + 1])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(max_diff, (
        ([0, 1, 2, 3, 4, 5, 6], 6),
        ([-0, 1, 2, -3, 4, 5, -6], 11),
        ([0, 1, 2, 3, 4, 5, 16], 16),
        ([16], 0),
        ([], 0),
    ))
