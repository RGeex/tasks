"""
Вам дан массив целых чисел нечетной длины , в котором все числа одинаковы,
за исключением одного единственного числа.

Дополните метод, который принимает такой массив и возвращает единственное отличающееся число.

Входной массив всегда будет корректным! (нечетная длина >= 3)

Примеры
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3


"""
import unittest
from typing import Any, Callable, List, Tuple
from functools import reduce


def stray(arr: List[int]) -> int:
    """
    Определяет единственное числдо, отличающееся от остальных.
    """
    return [(res := res ^ x) if i else (res := x) for i, x in enumerate(arr)] and res


def stray_2(arr: List[int]) -> int:
    """
    Определяет единственное числдо, отличающееся от остальных.
    """
    return reduce(lambda prev, curr: prev ^ curr, arr)


def stray_3(arr: List[int]) -> int:
    """
    Определяет единственное числдо, отличающееся от остальных.
    """
    return min(set(arr), key=arr.count)


def stray_4(arr: List[int]) -> int:
    """
    Определяет единственное числдо, отличающееся от остальных.
    """
    arr.sort()
    return arr[-1] if arr[0] == arr[1] else arr[0]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(stray, (
        ([1, 1, 1, 1, 1, 1, 2], 2),
        ([2, 3, 2, 2, 2], 3),
        ([3, 2, 2, 2, 2], 3),
    ))
    test(stray_2, (
        ([1, 1, 1, 1, 1, 1, 2], 2),
        ([2, 3, 2, 2, 2], 3),
        ([3, 2, 2, 2, 2], 3),
    ))
    test(stray_3, (
        ([1, 1, 1, 1, 1, 1, 2], 2),
        ([2, 3, 2, 2, 2], 3),
        ([3, 2, 2, 2, 2], 3),
    ))
    test(stray_4, (
        ([1, 1, 1, 1, 1, 1, 2], 2),
        ([2, 3, 2, 2, 2], 3),
        ([3, 2, 2, 2, 2], 3),
    ))
