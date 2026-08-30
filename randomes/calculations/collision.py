"""
Создайте функцию для определения того, сталкиваются ли две окружности.
В качестве параметров вам будут предоставлены координаты обеих окружностей, а также их радиусы:

def collision(x1, y1, radius1, x2, y2, radius2):  
  # collision?
Если обнаружено столкновение, вернуть true. В противном случае вернуть false.
"""
import unittest
from typing import Any, Callable, Tuple
from math import sqrt, dist


def collision(x1: int | float, y1: int | float, radius1: int | float, x2: int | float, y2: int | float, radius2: int | float) -> bool:
    """
    Определяет пересекаются ли окружности.
    """
    return radius1+radius2 >= dist((x1, y1), (x2, y2))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(collision, (
        ((1, 1, 1, 1.1, 1.1, 0.1), True),
        ((-1, 1, 10, -10.1, 1.1, 1), True),
        ((-5, 5, 5.0001, 5, -5, 5*sqrt(5)), True),
        ((1, 1, 0.01, 1, 1.1, 0.01), False),
        ((-1, 1, 6, -10.1, 1.1, 1), False),
        ((-5, 5, 5.0001, 5, -5, 4*sqrt(5)), False),
    ))
