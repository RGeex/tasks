"""
Напишите функцию, которая принимает на вход массив массивов чисел и возвращает сумму средних
значений этих массивов.
Пример

[
  [3, 4, 1, 3, 5, 1, 4], #  (3 + 4 + 1 + 3 + 5 + 1 + 4) / 7 =  3
  [21, 54, 33, 21, 77]   # (21 + 54 + 33 + 21 + 77)     / 5 = 41.2
]
result: 3 + 41.2 = 44.2
"""
import unittest
from typing import Any, Callable, List, Tuple


def sum_average(lists: List[List[int]]) -> float:
    """
    Подсчитывает сумму средних значений списка.
    """
    return sum(sum(x) / len(x) for x in lists)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sum_average, (
        ([[1, 2, 2, 1], [2, 2, 2, 1]], 3.25),
        ([[52, 64, 84, 21, 54], [44, 87, 46, 90, 43]], 117),
        ([[44, 76, 12], [96, 12, 34, 53, 76, 34, 56, 86, 21], [34, 65, 34, 76, 34, 87, 34]], 148),
        ([[3, 4, 1, 3, 5, 1, 4], [21, 54, 33, 21, 76]], 44),
        ([[-4, 3, -8, -2], [2, 9, 1, -5], [-7, -2, -6, -4]], -5.75),
    ))
