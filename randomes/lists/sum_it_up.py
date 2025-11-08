"""
Вам нужно сложить массив разных чисел. Но есть одна проблема: все эти числа имеют разные основания. Например:

You get an array of numbers with their base as an input:

[["101",16],["7640",8],["1",9]]
На выходе должна быть сумма в виде целого значения по основанию 10, то есть согласно примеру это будет:

4258

A few more examples:
[["101",2], ["10",8]] --> 13
[["ABC",16], ["11",2]] --> 2751
Основания могут быть от 2 до 36 (2 <= основание <= 36)
"""
import typing
import unittest


def sum_it_up(numbers_with_bases: list[list[str, int]]) -> int:
    """
    Вычисляет сумму чисел с разным основанием.
    """
    return sum([int(a, b) for a, b in numbers_with_bases])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sum_it_up, (
        ([["101",2], ["10",8]],13),
        ([["ABC",16], ["11",2]],2751),
        ([["101",16],["7640",8],["1",9]],4258),
    ))
