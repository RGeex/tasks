"""
Описание

Дан список целых чисел (возможно, включающий повторяющиеся) и положительное целое число.
k(> 0), найдите минимальное и максимальное возможное произведение k элементы взяты из списка.

Если вы не можете взять достаточно элементов из списка ( k> размер списка), вернуть None/ nil.
Примеры

numbers = [1, -2, -3, 4, 6, 7]

k = 1  ==>  -3, 7
k = 2  ==>  -21, 42    # -3*7, 6*7
k = 3  ==>  -126, 168  # -3*6*7, 4*6*7
k = 7  ==>  None       # there are only 6 elements in the list

Примечание: тестовые списки достаточно малы (до 20 элементов),
что позволяет использовать простой подход.
"""
import unittest
from typing import Any, Callable, List, Optional, Tuple
from operator import mul
from functools import reduce
from itertools import combinations


def find_min_max_product(arr: List[int], k: int) -> Optional[Tuple[int, int]]:
    """
    Возвращает минимальное и максимальное произведение из списка.
    """
    if len(arr) >= k:
        lst = sorted(reduce(mul, x) for x in combinations(arr, k))
        return lst[0], lst[-1]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_min_max_product, (
        (([1, -2, -3, 4, 6, 7], 1), (-3, 7)),
        (([1, -2, -3, 4, 6, 7], 2), (-21, 42)),
        (([1, -2, -3, 4, 6, 7], 3), (-126, 168)),
        (([1, -2, -3, 4, 6, 7], 7), None),
    ))
