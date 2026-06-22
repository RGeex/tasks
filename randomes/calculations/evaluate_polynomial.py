"""
Дан массив коэффициентов, представляющих многочлен, и его значение. xВычислите значение многочлена.
Коэффициенты упорядочены от члена наивысшей степени к постоянному члену.

Например: [2,3,4]

Представлять: 2x² + 3x + 4
Задача:

Реализуйте функцию, которая вычисляет значение многочлена в заданной точке. x.
Примеры:

evaluate([2, 3, 4], 2) == 18 потому что 2·2² + 3·2 + 4 = 8 + 6 + 4 = 18.
Примечания:

    Многочлен может содержать большое количество коэффициентов.
    Коэффициенты могут быть положительными, отрицательными или равными нулю.
    xможет быть положительным, отрицательным или равным нулю.
    Ваше решение должно быть достаточно эффективным для обработки больших объемов входных данных.



"""
import unittest
from typing import Any, Callable, Tuple


def evaluate_polynomial(coefficients: list[int], x: int) -> int:
    """
    ычисляет значение многочлена в заданной точке. x
    """
    return sum(n * x ** i for i, n in enumerate(coefficients[::-1]))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(evaluate_polynomial, (
        (([2, 3, 4], 2), 18),
        (([1, 0, -1], 3), 8),
        (([5], 100), 5),
    ))
