"""
Вам будет предоставлены значения arrayи limit.
Необходимо проверить, что все значения в массиве меньше или равны
предельному значению. Если это так, верните true. В противном случае верните false.

Можно предположить, что все значения в массиве — числа.
"""
import unittest
from typing import Any, Callable, List, Tuple


def small_enough(array: List[int], limit: int) -> bool:
    """
    Проверяет все ли числа из списка не превышают лимит.
    """
    return not next((1 for n in array if n > limit), 0)


def small_enough_2(array: List[int], limit: int) -> bool:
    """
    Проверяет все ли числа из списка не превышают лимит.
    """
    return all(map(limit.__ge__, array))


def small_enough_3(array: List[int], limit: int) -> bool:
    """
    Проверяет все ли числа из списка не превышают лимит.
    """
    return all(n <= limit for n in array)


def small_enough_4(array: List[int], limit: int) -> bool:
    """
    Проверяет все ли числа из списка не превышают лимит.
    """
    return max(array) <= limit


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(small_enough, (
        ([[66, 101], 200], True),
        ([[78, 117, 110, 99, 104, 117, 107, 115], 100], False),
        ([[101, 45, 75, 105, 99, 107], 107], True),
        ([[80, 117, 115, 104, 45, 85, 112, 115], 120], True),
        ([[1, 1, 1, 1, 1, 2], 1], False),
        ([[78, 33, 22, 44, 88, 9, 6], 87], False),
        ([[1, 2, 3, 4, 5, 6, 7, 8, 9], 10], True),
        ([[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 12], True),
    ))
    test(small_enough_2, (
        ([[66, 101], 200], True),
        ([[78, 117, 110, 99, 104, 117, 107, 115], 100], False),
        ([[101, 45, 75, 105, 99, 107], 107], True),
        ([[80, 117, 115, 104, 45, 85, 112, 115], 120], True),
        ([[1, 1, 1, 1, 1, 2], 1], False),
        ([[78, 33, 22, 44, 88, 9, 6], 87], False),
        ([[1, 2, 3, 4, 5, 6, 7, 8, 9], 10], True),
        ([[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 12], True),
    ))
    test(small_enough_3, (
        ([[66, 101], 200], True),
        ([[78, 117, 110, 99, 104, 117, 107, 115], 100], False),
        ([[101, 45, 75, 105, 99, 107], 107], True),
        ([[80, 117, 115, 104, 45, 85, 112, 115], 120], True),
        ([[1, 1, 1, 1, 1, 2], 1], False),
        ([[78, 33, 22, 44, 88, 9, 6], 87], False),
        ([[1, 2, 3, 4, 5, 6, 7, 8, 9], 10], True),
        ([[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 12], True),
    ))
    test(small_enough_4, (
        ([[66, 101], 200], True),
        ([[78, 117, 110, 99, 104, 117, 107, 115], 100], False),
        ([[101, 45, 75, 105, 99, 107], 107], True),
        ([[80, 117, 115, 104, 45, 85, 112, 115], 120], True),
        ([[1, 1, 1, 1, 1, 2], 1], False),
        ([[78, 33, 22, 44, 88, 9, 6], 87], False),
        ([[1, 2, 3, 4, 5, 6, 7, 8, 9], 10], True),
        ([[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 12], True),
    ))
