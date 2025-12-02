"""
Вам дан массив неотрицательных целых чисел, ваша задача — завершить ряд от 0
до наибольшего числа в массиве.

Если числа в предоставленной последовательности не упорядочены, вы должны
упорядочить их, но если значение повторяется, то вы должны вернуть
последовательность только с одним элементом, и значение этого элемента
должно быть равно 0. Например:

inputs        outputs
[2,1]     ->  [0,1,2]
[1,4,4,6] ->  [0]

Примечания: все числа — положительные целые числа.

Это набор примеров выходных данных, основанных на последовательности входных
данных.

inputs        outputs
[0,1]   ->    [0,1]
[1,4,6] ->    [0,1,2,3,4,5,6]
[3,4,5] ->    [0,1,2,3,4,5]
[0,1,0] ->    [0]
"""
import typing
import unittest


def complete_series(seq: list[int]) -> list[int]:
    """
    Восполняет недостающие элементы последовательности, если среди них нет повторяющихся, иначе [0].
    """
    return list(range(max(seq) + 1)) if len(seq) == len(set(seq)) else [0]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(complete_series, (
        ([0, 1], [0, 1]),
        ([1, 4, 6], [0, 1, 2, 3, 4, 5, 6]),
        ([3, 4, 5], [0, 1, 2, 3, 4, 5]),
        ([2, 1], [0, 1, 2]),
        ([1, 4, 4, 6], [0]),
    ))
