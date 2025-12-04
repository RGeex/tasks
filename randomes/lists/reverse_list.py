"""
Напишите функцию reverseList, которая просто переворачивает списки.
"""
import unittest
from typing import Any, Callable, List, Tuple


def reverse_list(lst: List[Any]) -> List[Any]:
    """
    Переворачивает списки.
    """
    return lst[::-1]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(reverse_list, (
        ([], []),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([2, 4, 5, 6], [6, 5, 4, 2]),
    ))
