"""
Напишите функцию, которая принимает число в качестве входных данных и возвращает
сумму абсолютных значений каждой из десятичных цифр этого числа.

Например: ( Вход --> Выход )

10 --> 1
99 --> 18
-32 --> 5

Предположим, что все числа на входе будут целыми.
"""
import unittest
from typing import Any, Callable, Tuple


def sum_digits(number: int) -> int:
    """
    Суммирует все цифры заданного числа.
    """
    return sum(map(int, str(abs(number))))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sum_digits, (
        (10, 1),
        (99, 18),
        (-32, 5),
        (1234567890, 45),
        (0, 0),
        (666, 18),
        (100000002, 3),
        (800000009, 17),
    ))
