"""
Создайте функцию `add` , которая сможет непрерывно суммировать элементы списка и
возвращать новый список сумм.

Например:

add [1,2,3,4,5] == [1, 3, 6, 10, 15], because it's calculated like
this : [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4, 1 + 2 + 3 + 4 + 5]
"""
import unittest
from typing import Any, Callable, Tuple


def add(lst: list[int]) -> list[int]:
    """
    Суммирует последовательно элементы списка.
    """
    return [sum(lst[:i + 1]) for i in range(len(lst))]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(add, (
        ([1, 2, 3, 4, 5], [1, 3, 6, 10, 15]),
        ([20, 21, 22, 23, 24, 25], [20, 41, 63, 86, 110, 135]),
        ([2, 4, 6, 8, 10], [2, 6, 12, 20, 30]),
        ([1, 4, 9, 16, 25, 36], [1, 5, 14, 30, 55, 91]),
        ([1, 8, 27, 64, 125], [1, 9, 36, 100, 225]),
        ([5, 10, 15, 20, 25, 30, 35, 40], [5, 15, 30, 50, 75, 105, 140, 180]),
        ([6, 12, 18, 24, 30, 36, 42], [6, 18, 36, 60, 90, 126, 168]),
        ([7, 14, 21, 28, 35, 42, 49, 56], [7, 21, 42, 70, 105, 147, 196, 252]),
        ([8, 16, 24, 32, 40, 48, 56, 64], [8, 24, 48, 80, 120, 168, 224, 288]),
        ([9, 18, 27, 36, 45, 54], [9, 27, 54, 90, 135, 189]),
    ))
