"""
Реализуйте функцию, которая отфильтровывает значения массива, удовлетворяющие заданному предикату.

reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)  =>  [1, 3, 5]
"""
import typing
import unittest


def reject(seq: list[int|str], predicate: typing.Callable) -> list[int|str]:
    """
    отфильтровывает список по предикату.
    """
    return [x for x in seq if not predicate(x)]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(reject, (
        (([1, 2, 3, 4, 5, 6], lambda x: x%2==0), [1, 3, 5]),
        ((['a', 'b', 3, 'd'], lambda x: type(x)==int), ['a', 'b', 'd']),
        ((['a', 'b', 3, 'd'], lambda x: type(x)==str), [3]),
    ))
