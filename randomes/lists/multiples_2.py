"""
При наличии 3 положительных параметров a, b, limit, возвращаются все положительные числа,
кратные обоим a параметрам и , bвплоть до limit.

Примеры
1, 5, 15 --> [5, 10, 15]
3, 5, 15 --> [15]
3, 5, 40 --> [15, 30]
2, 4, 40 --> [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
"""
import unittest
from typing import Any, Callable, List, Tuple


def multiples(a: int, b: int, limit: int) -> List[int]:
    """
    Поиск всех чисел в диапазоне, кратных a и b.
    """
    return [x for x in range(1, limit + 1) if not x % a and not x % b]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(multiples, (
        ((2, 4, 40), [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]),
        ((3, 4, 40), [12, 24, 36]),
        ((7, 4, 80), [28, 56]),
        ((7, 4, 20), []),
        ((7, 5, 200), [35, 70, 105, 140, 175]),
        ((21, 5, 800), [105, 210, 315, 420, 525, 630, 735]),
    ))
