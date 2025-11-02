"""
Напишите функцию, которая принимает массив уникальных целых чисел и возвращает минимальное количество целых чисел,
необходимое для того, чтобы сделать значения массива последовательными от наименьшего числа до наибольшего.

Пример
[4, 8, 6] --> 2
Because 5 and 7 need to be added to have [4, 5, 6, 7, 8]

[-1, -5] --> 3
Because -2, -3, -4 need to be added to have [-5, -4, -3, -2, -1]

[1] --> 0
[]  --> 0
"""
import typing
import unittest


def consecutive(arr: list[int]) -> int:
    """
    Определяет, кол-во недостающих элементов списка для полной последовательности.
    """
    return len(arr) > 1 and len(set(range(*sorted(arr)[::len(arr) - 1])) - set(arr))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(consecutive, (
        ([4,8,6], 2),
        ([1,2,3,4], 0),
        ([], 0),
        ([1], 0),
        ([-10], 0),
        ([1,-1], 1),
        ([-10,-9], 0),
        ([0], 0),
        ([10,-10], 19),
        ([-10,10], 19),
    ))
