"""
Нет истории

Нет описания

Только путем размышления и проверки.

Посмотрите на результаты тестовых случаев и попробуйте угадать код!

"""
import unittest
from typing import Any, Callable, Tuple


def testit(n: int) -> int:
    """
    Определяет кол-во бит в числе.
    """
    return bin(n).count('1')


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(testit, (
        (0, 0),
        (0, 0),
        (2, 1),
        (3, 2),
        (4, 1),
        (5, 2),
        (6, 2),
        (7, 3),
        (8, 1),
        (9, 2),
        (10, 2),
        (100, 3),
        (1000, 6),
        (10000, 5),
    ))
