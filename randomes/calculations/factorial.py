"""
В математике факториал неотрицательного целого числа n, обозначаемый n!, — это произведение всех
положительных целых чисел, меньших или равных n. Например: 5! = 5 * 4 * 3 * 2 * 1 = 120.
По соглашению, значение 0! равно 1.

Напишите функцию для вычисления факториала для заданного входного значения. Если входное значение
меньше 0 или больше 12, сгенерируйте исключение соответствующего типа.
ArgumentOutOfRangeException(C#) или IllegalArgumentException(Java) или RangeException(PHP) или
бросить RangeError(JavaScript) или ValueError(Python) или вернуть -1(С).

"""
import unittest
from typing import Any, Callable, Tuple


def factorial(n: int) -> int:
    """
    Определение фактиориала для числа.
    """
    if 0 <= n <= 12:
        return factorial(n - 1) * n if n else 1
    raise ValueError('Only for: 0 <= n <= 12')


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(factorial, (
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
    ))
