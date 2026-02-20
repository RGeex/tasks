"""
Последовательность периметра

Показаны первые три этапа последовательности.

блоки

Размер блока равен a к a и a ≥ 1.

Каков периметр... nth фигура в последовательности ( n ≥ 1) ?

"""
import unittest
from typing import Any, Callable, Tuple


def perimeter_sequence(a: int, n: int) -> int:
    """
    Вычисляет периметр фигуры в последовательности.
    """
    return 4 * a * n


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(perimeter_sequence, (
        ((1, 3), 12),
    ))
