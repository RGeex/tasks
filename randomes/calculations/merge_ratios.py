"""
2 отношения, представленные в виде строк в форме A:B и B:C.

например 12:4 3:7

Ваша программа должна возвращать соотношение A:B:C в простейшей форме.

например 12:4 3:7 ---> 9:3:7

Дано, что отношения не представлены в простейшей форме. A, B и C всегда находятся в диапазоне от 1 до 1e5.

возвращает строку в формате "9:3:7"
"""
import unittest
from typing import Any, Callable, Tuple
from math import gcd


def merge_ratios(ratio1: str, ratio2: str) -> str:
    """
    Определяет соотношения.
    """
    a, b, c, d = map(int, ratio1.split(':') + ratio2.split(':'))
    g = gcd(a * c, b * c, b * d)
    return f'{a * c // g}:{b * c // g}:{b * d // g}'


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(merge_ratios, (
        (("12:4", "3:7"), "9:3:7"),
        (("64:32", "64:14"), "64:32:7"),
        (("6937:3221", "7:108"), "48559:22547:347868"),
    ))
