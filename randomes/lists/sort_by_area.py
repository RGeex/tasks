"""
В этой ката вам будет дана последовательность размеров прямоугольников
(последовательность с шириной и длиной) и кругов (радиус - просто число).
Ваша задача — вернуть новую последовательность измерений,
отсортированную по площади в порядке возрастания.

Например,

seq = [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ] # [ rectangle, circle, circle, rectangle ]
sort_by_area(seq) => [ ( 1.342, 3.212 ), 1.23, ( 4.23, 6.43 ), 3.444 ]

"""
import unittest
from typing import Any, Callable, List, Tuple


def sort_by_area(seq: List[int | float | Tuple[int | float]]) -> List[int | float | Tuple[int | float]]:
    """
    Сортирует фигуры по их площади.
    """
    return sorted(seq, key=lambda x: x[0] * x[1] if isinstance(x, tuple) else 3.14 * x ** 2)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_by_area, (
        ([(4.23, 6.43), 1.23, 3.444, (1.342, 3.212)], [(1.342, 3.212), 1.23, (4.23, 6.43), 3.444]),
        ([(2, 5), 6], [(2, 5), 6]),
        ([], []),
    ))
