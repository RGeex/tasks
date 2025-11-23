"""
Учитывая список целочисленных значений, ваша задача — вернуть сумму значений.
Однако если одно и то же целое значение встречается в списке несколько раз,
вы можете учесть его в сумме только один раз.

Например:

[ 1, 2, 3] ==> 6

[ 1, 3, 8, 1, 8] ==> 12

[ -1, -1, 5, 2, -7] ==> -1

[] ==> None
"""
import typing
import unittest


def unique_sum(lst: list[int]) -> int | None:
    """
    Вычисляет сумму уникальных значений списка, если он не пустой.
    """
    return sum(set(lst)) if lst else None


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(unique_sum, (
        ([1,2,3], 6),
        ([1,3,8,1,8], 12),
        ([-1,-1,5,2,-7],-1),
    ))
