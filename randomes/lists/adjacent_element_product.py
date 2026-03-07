"""
Задача

Дан массив целых чисел. Найдите максимальное произведение, полученное при умножении двух соседних
чисел в массиве. Обратите внимание, что размер массива не менее 2 и содержит смесь положительных,
отрицательных целых чисел, а также нулей.
"""
import unittest
from typing import Any, Callable, List, Tuple


def adjacent_element_product(array: List[int]) -> int:
    """
    Поиск максимального произведения чисел списка, стоящих рядом друг с другом.
    """
    return max(a * b for a, b in zip(array, array[1:]))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(adjacent_element_product, (
        ([5, 8], 40),
        ([1, 2, 3], 6),
        ([1, 5, 10, 9], 90),
        ([4, 12, 3, 1, 5], 48),
        ([5, 1, 2, 3, 1, 4], 6),
        ([3, 6, -2, -5, 7, 3], 21),
        ([9, 5, 10, 2, 24, -1, -48], 50),
        ([5, 6, -4, 2, 3, 2, -23], 30),
        ([-23, 4, -5, 99, -27, 329, -2, 7, -921], -14),
        ([5, 1, 2, 3, 1, 4], 6),
        ([1, 0, 1, 0, 1000], 0),
        ([1, 2, 3, 0], 6),
    ))
