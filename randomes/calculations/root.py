"""
Даны два числа xи n, вычислите (положительный) корень n-й степени из x; это означает, что ,
будучи r = result,r^n = x

Примеры
x = 4     n = 2  -->  2    # the square root of 4 is 2     2^2 = 4
x = 8     n = 3  -->  2    # the cube root of 8 is 2       2^3 = 8
x = 256   n = 4  -->  4    # the 4th root of 256 is 4      4^4 = 256
x = 9     n = 2  -->  3    # the square root of 9 is 3     3^2 = 9
x = 6.25  n = 2  -->  2.5  #                             2.5^2 = 6.25
Примечания:
4 <= x < 10 ^ 20
4 <= n <= 50
Удачи!
"""
import unittest
from typing import Any, Callable, Tuple


def root(x: int | float, n: int) -> float:
    """
    Вычисляет степень возведения.
    """
    return x ** (1 / n)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(root, (
        ((8, 3), 2),
        ((6.25, 2), 2.5),
    ))
