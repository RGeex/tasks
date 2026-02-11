"""
Нет истории

Нет описания

Только путем размышления и проверки.

Посмотрите на результат тестового примера и угадайте код!
"""
import unittest
from typing import Any, Callable, List, Tuple


def testit(a: List[int], b: List[int]) -> List[int]:
    """
    Объединяет в отсортированный список, уникальные элементы переданных списков.
    """
    return sorted(list(set(a)) + list(set(b)))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(testit, (
        (([0], [1]), [0, 1]),
        (([1, 2], [3, 4]), [1, 2, 3, 4]),
        (([1], [2, 3, 4]), [1, 2, 3, 4]),
        (([1, 2, 3], [4]), [1, 2, 3, 4]),
        (([1, 2], [1, 2]), [1, 1, 2, 2]),
    ))
