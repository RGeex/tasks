"""
Прямоугольник можно определить двумя факторами: высотой и шириной.

Его площадь определяется как произведение двух величин: высота * ширина.

Его периметр равен сумме четырех сторон: высота + высота + ширина + ширина.

Можно создавать прямоугольники одинаковой площади, но с разными периметрами.
Например, при площади 45, возможные значения высоты, ширины и, как следствие,
периметра будут следующими:

(1, 45) = 92

(9, 5) = 28

(15, 3) = 36

Обратите внимание, что (6, 7,5) также имеет площадь 45, но в этом задании она
отбрасывается, поскольку её ширина не является целой.

Задача состоит в том, чтобы написать функцию, которая, получив на вход площадь
в виде положительного целого числа, возвращает наименьший возможный периметр
прямоугольника со сторонами, равными целому числу.
Диапазон входного сигнала:

1 <= площадь <= 5 x 10 ^ 10

"""
import unittest
from typing import Any, Callable, Tuple


def minimum_perimeter(n: int) -> int:
    """
    Определяет минимальный периметр прямоугольника, из значения его площади.
    """
    return min(i * 2 + n // i * 2 for i in range(1, n // 2) if not n % i)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(minimum_perimeter, (
        (45, 28),
        (30, 22),
        (81, 36),
        (89, 180),
    ))
