"""
Напишите функцию, которая принимает в качестве аргумента список, содержащий не менее четырех
элементов, и возвращает список из двух или трех средних элементов в обратном порядке.
"""
import unittest
from typing import Any, Callable, List, Tuple


def reverse_middle(lst: List[Any]) -> List[Any]:
    """
    Возвращает список из двух или трех средних элементов в обратном порядке.
    """
    return lst[len(lst) // 2 - 1:len(lst) // 2 + 1 + len(lst) % 2][::-1]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(reverse_middle, (
        ([4, 3, 100, 1], [100, 3]),
        ([1, False, 'string', {}, 7.43], [{}, 'string', False]),
    ))
