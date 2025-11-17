"""
Дана квадратная матрица (т.е. массив подмассивов), найдите сумму значений
первого значения первого массива, второго значения второго массива,
третьего значения третьего массива и т.д.

Примеры
array = [[1, 2],
         [3, 4]]

diagonal sum: 1 + 4 = 5
array = [[5, 9, 1, 0],
         [8, 7, 2, 3],
         [1, 4, 1, 9],
         [2, 3, 8, 2]]

diagonal sum: 5 + 7 + 1 + 2 = 15
"""
import typing
import unittest


def diagonal_sum(array: list[list[int]]) -> int:
    """
    Вычисляет сумму чисел диагонали мастрицы.
    """
    return sum(x[i] for i, x in enumerate(array))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(diagonal_sum, (
    ([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9] ], 15),
    ([
        [1, 2],
        [3, 4] ], 5),
    ([
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16] ], 34),
    ))
