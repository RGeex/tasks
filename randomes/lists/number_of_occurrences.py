"""
Напишите функцию, которая возвращает количество вхождений элемента в массиве.

Примеры
sample = [0, 1, 2, 2, 3]
number_of_occurrences(0, sample) == 1
number_of_occurrences(4, sample) == 0
number_of_occurrences(2, sample) == 2
number_of_occurrences(3, sample) == 1
"""
import unittest
from typing import Any, Callable, List, Tuple


def number_of_occurrences(element: int, sample: List[int]) -> int:
    """
    Подсчитывает кол-во вхождений элемента в списке.
    """
    return sample.count(element)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    sample = [0, 1, 2, 2, 3]
    test(number_of_occurrences, (
        ((4, sample), 0),
        ((6, sample), 0),
        ((-1, sample), 0),
        ((0, sample), 1),
        ((2, sample), 2),
        ((3, sample), 1),
    ))
