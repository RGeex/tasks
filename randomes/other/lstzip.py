"""
Писать

lstzip
Эта функция объединяет соответствующие элементы двух последовательностей,
используя заданную функцию-селектор fn(например, a blockв Ruby).

Например:

a = [1, 2, 3, 4, 5]
b = ['a', 'b']
lstzip(a,b, lambda a,b: str(a)+str(b))

a = [1, 2, 3, 4, 5]
b = ['a','b','c','d','e']
lstzip(a,b, lambda a, b: a * ord(b[0]))
Если массивы имеют разную длину, дойдите до минимальной длины и остановитесь.
"""
import unittest
from typing import Any, Callable, Tuple
from itertools import starmap


def lstzip(a: list, b: list, fn: Callable) -> list:
    """
    Объединяет соответствующие элементы двух последовательностей, используя заданную функцию-селектор.
    """
    return list(starmap(fn, zip(a, b)))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = ['a','b','c','d','e']
    test(lstzip, (
        ((a, b, lambda a, b: str(a) + str(b)), ["1a", "2b", "3c", "4d", "5e"]),
        ((b, a, lambda a, b: str(a) + str(b)), ["a1", "b2", "c3", "d4", "e5"]),
        ((b, lstzip(a, b, lambda a, b: a * ord(b[0])), lambda a, b: str(a) + str(b)), ["a97", "b196", "c297", "d400", "e505"]),
    ))
