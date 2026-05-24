"""
Реализуйте функцию для вычисления расстояния между двумя точками в n-мерном пространстве.
Обе точки будут переданы в вашу функцию в виде массивов одинаковой длины.

"""
import unittest
from typing import Any, Callable, List, Tuple


def euclidean_distance(point1: List[int], point2: List[int]) -> float:
    """
    Вычисляет расстояние между двумя точками в n-мерном пространстве.
    """
    return sum([(a - b) ** 2 for a, b in zip(point1, point2)]) ** 0.5


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(euclidean_distance, (
        (([-1], [2]), 3.0),
        (([-1, 2], [2, 4]), 3.605551275463989),
        (([-1, 2, 5], [2, 4, 9]), 5.385164807134504),
    ))
