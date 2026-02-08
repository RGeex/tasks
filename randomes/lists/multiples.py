"""
Реализуйте функцию, которая принимает два числа. m и n
и возвращает массив первых mкратные действительного числа n
Предположим, что mявляется положительным целым числом.

Бывший.

(3, 5.0) --> [5.0, 10.0, 15.0]


"""
import unittest
from typing import Any, Callable, List, Tuple


def multiples(m: int, n: int | float) -> list[int] | list[float]:
    """
    Создает последовательность чисел кратных заданному числу.
    """
    return [n * i for i in range(1, m + 1)]


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
        ((3, 5), [5, 10, 15]),
        ((1, 3.14), [3.14]),
        ((5, -1), [-1, -2, -3, -4, -5]),
    ))
