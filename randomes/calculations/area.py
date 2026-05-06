"""
Найдите площадь прямоугольника, зная его диагональ и одну из сторон.
Если диагональ меньше или равна длине стороны, верните результат. "Not a rectangle".
"""
import unittest
from typing import Any, Callable, Tuple


def area(d: int, l: int) -> int | float | str:
    """
    Вычисляет площадь прямоугольника, если это возможно.
    """
    return d <= l and 'Not a rectangle' or l * ((d * d - l * l) ** .5)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(area, (
        ((5, 4), 12),
        ((10, 6), 48),
        ((13, 5), 60),
        ((12, 5), 54.54356057317857),
        ((5, 5), "Not a rectangle"),
        ((3, 5), "Not a rectangle"),
    ))
