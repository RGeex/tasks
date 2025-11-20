"""
Найти последний элемент заданных аргументов. Если передан один аргумент,
представляющий собой список/массив или строку, вернуть его последний элемент.
Гарантируется, что будет хотя бы один аргумент, и что массивы/списки/строки с
одним аргументом не будут пустыми.

Примеры
last(5)               ==> 5
last([1, 2, 3, 4])    ==>  4
last("xyz")           ==> "z"
last(1, 2, 3, 4)      ==>  4
last([1, 2], [3, 4])  ==>  [3, 4]
last([[1, 2], [3, 4]])  ==>  [3, 4]
"""
import typing
import unittest


def last(*args: typing.Any):
    """
    Возвращает последний элемент переданных данных.
    """
    return args[-1] if len(args) > 1 or len(args) == 1 and isinstance(args[-1], int) else args[-1][-1]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val)
             for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(
        type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(last, (
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
        ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 10),
        (list("abckxyz"), "z"),
        ("abckxyz", "z"),
        (("a", "b", "c", "z"), "z"),
        (5, 5),
        ((123, [4, 5, 6]), [4, 5, 6]),
    ))
