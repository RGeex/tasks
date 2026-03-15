"""
Магическая сумма троек вычисляется в массиве путем сложения нечетных чисел, включающих эту цифру. 3.

Завершите функцию, которая принимает массив целых чисел и возвращает его магическую сумму, равную 3.

Пример: [3, 12, 5, 8, 30, 13]результаты в 16( 3+ 13)

Если такого числа в массиве нет, 0следует вернуть.

"""
import unittest
from typing import Any, Callable, List, Tuple


def magic_sum(arr: List[int]) -> int:
    """
    Суммирует нечетные числа содержашие цифру 3.
    """
    return sum(n for n in arr if n % 2 and '3' in str(n))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(magic_sum, (
        ([3], 3),
        ([3, 13], 16),
        ([30, 34, 330], 0),
        ([3, 12, 5, 8, 30, 13], 16),
        ([], 0),
    ))
