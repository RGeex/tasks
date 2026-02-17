"""
Предположим, у меня есть два вектора: (a1, a2, a3, ..., aN) и (b1, b2, b3, ..., bN)
Скалярное произведение этих двух векторов определяется следующим образом:

a1*b1 + a2*b2 + a3*b3 + ... + aN*bN

Векторы считаются ортогональными, если скалярное произведение равно нулю.

Завершите функцию, которая принимает две последовательности в качестве входных данных и
возвращает результат. trueесли векторы ортогональны, и falseЕсли это не так,
то последовательности всегда будут правильно отформатированы и иметь одинаковую длину,
поэтому нет необходимости проверять их предварительно.
Примеры

[1, 1, 1], [2, 5, 7]        --> false
[1, 0, 0, 1], [0, 1, 1, 0]  --> true


"""
import unittest
from typing import Any, Callable, List, Tuple


def is_orthogonal(u: List[int], v: List[int]) -> bool:
    """
    Определяет, являются ли векторы ортогональными.
    """
    return not sum(a * b for a, b in zip(u, v))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_orthogonal, (
        (([1, 2], [2, 1]), False),
        (([1, -2], [2, 1]), True),
        (([7, 8], [7, -6]), False),
        (([-13, -26], [-8, 4]), True),
        (([1, 2, 3], [0, -3, 2]), True),
        (([3, 4, 5], [6, 7, -8]), False),
        (([3, -4, -5], [-4, -3, 0]), True),
        (([1, -2, 3, -4], [-4, 3, 2, -1]), True),
        (([2, 4, 5, 6, 7], [-14, -12, 0, 8, 4]), True),
        (([5, 10, 1, 20, 2], [-2, -20, -1, 10, 5]), False),
    ))
